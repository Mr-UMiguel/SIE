## Módulos propios
from SECTOR_REAL.db import get_db
from SECTOR_REAL.runMacro import run_excel_macro

# Prefect.io modules
from prefect import task

# Other modules
import pandas as pd
import datetime
import time
import xlwings as xw



@task(log_stdout=True, max_retries=1,retry_delay=datetime.timedelta(seconds=10))
def Extract(function, download_path:str):
    r = function(download_path)
    return r

@task(log_stdout=True)
def Transform(function,file_name:str,flar_name:str,
            download_path:str,file_macro:str,refAreaID:str,flarID:str):

    ### Renombramos el archivo 
    state = function(file_name,flar_name,download_path)

    ### Si al renombrar al archivo todo sale bien entonces ejecutamos la macro
    if state == True:
        rango = run_excel_macro(file_macro)

    ## el rango (número de observaciones) debe ser siempre mayor a dos
    if int(rango) <= 2:
        raise Exception("Failed to compile macro: observations doesn't exist")

    ## Creamos la conexión a la base de datos sieDB
    cnxn, cursor = get_db()

    ## Si el rango existe 
    # para metrizamos una condición para ejecutar o no ejecutar el job en SQL
    # update_status=0 No actualizar
    # update_status=1 Nuevas observaciones
    # update_status=2 Observaciones actuales actualizadas (actualización hacia atrás)
    update_status = 0

    if rango != None:
        ### Creamos la conexión a Excel y abrimos la macro 
        xl_app = xw.App(visible=False, add_book=False)
        wb = xl_app.books.open(file_macro)
        ws = wb.sheets[0]

        ## Buscamos en la base de datos el indicador correspondiente
        cursor.execute(
            """
            SELECT serie.serieID FROM serie 
            INNER JOIN indicator ON indicator.indicatorID = serie.indicatorID
            WHERE serie.refAreaID = ? and indicator.FLARID = ?
            """, refAreaID, flarID
        )

        serieID = cursor.fetchone()[0]

        ## Buscamos en la base de datos los valores observados
        cursor.execute(
            """
            SELECT timePeriod, obsValue FROM observation_value 
            WHERE observation_value.serieID = ?
            """, serieID
        ) 

        ### Validamos la información
        rows_db = cursor.fetchall() # Datos en la base sieDB
        rows_macro = ws.range(f"A11:B{rango}").options(ndim=2).value # Datos de la macro
        rows_macro = pd.Series(rows_macro).apply(lambda x: x.replace("P","") if "P" in x else x).tolist()
        rows_macro = pd.Series(rows_macro).apply(lambda x: x.replace("Q","") if "Q" in x else x).tolist()

        if len(rows_db) != len(rows_macro):
            if len(rows_macro) >= len(rows_db):
                update_status = 1
            else:
                rows_db_last4 = rows_db[-4:]
                rows_macro_last4 = rows_macro[-4:]
                if any(x[0] in [i[0] for i in rows_db_last4] for x in rows_macro_last4):
                    if any(x[1] in [i[1] for i in rows_db_last4] for x in rows_macro_last4):
                        update_status=2
        else:
            ## Comparamos los úlitmos 4 elementos ya que en series trimestres sería un año
            # y en series mensuales serían 4 meses
            # si son diferentes a los valores en base entonces se actualiza toda la serie 
            for rd,rm in zip(rows_db[-4:],rows_macro[-4:]):
                if rd != rm:
                    update_status = 2
                    break

        # Cerramos la macro y la conexión a Excel
        wb.close()
        xl_app.quit()
    else:
        raise Exception("File has not been compiled by Excel Macro or database connection doesn't exist")

    cursor.close()
    cnxn.close()
    
    return update_status



@task(log_stdout=True)
def Load(update_status:str, refAreaID:str, flarID:str):

    ## Verificamos que el update_status sea diferente de 0
    # Recrodemos que
    # update_status=0 No actualizar
    # update_status=1 Nuevas observaciones
    # update_status=2 Observaciones actuales actualizadas (actualización hacia atrás)
    if update_status != 0:
        try:
            # Ajuste de parámetros iniciales
            # Se utiliza un try ya que se espera captar algunos de los posibles errores
            # que suceden durante la ejecución del job que carga la información a SIEDB
            # Los errores más frecuentes hasta ahora son:
            # Tipo1: Que haya un error en el erchivo .xlsm que impide la lectura de los datos
            # Tipo2: Que el job se ejecute infintamente porque el archivo .xlsm puede estar abierto o dañado
            ## ----------------------------------------------------------------
            
            #Iniciamos la conexión a la base de datos
            cnxn, cursor = get_db()
            print("""
            Iniciando la ejecución del job
            ------------------------------
            """)
            #Cambiamos el estado de todos los indicadores a 2 en la tabla parámetros de SIEDB
            # si status = 2 no se ejecuta el job
            # si status = 1 se ejecuta el job
            cursor.execute(
            """
            UPDATE [SIEDB].[dbo].[parametros]
            SET status = 2
            """
            )
            #Cambiamos el estado del indicador a cargar
            cursor.execute("""
            UPDATE [SIEDB].[dbo].[parametros]
            SET STATUS=1
            WHERE country IN (?)
            AND fileName = ?
            """, refAreaID, f'{flarID}.xlsm'
            )
            # Enviamos la petición a la base
            cnxn.commit()


            #----------------------------------------------------------------
            #Ejecutamos el job
            cursor.execute("EXEC msdb.dbo.sp_start_job 'JobIndicadoresSIE'")
            cursor.close()
            cnxn.close()

        except Exception as e:

            ## Error de tipo 1
            # si al ejecutar el job se encuentra que ya está otro en ejcución se
            # evalúa si se demoró más de 4 minutos (tiempo promedio máximo que tarda la ejecución de un job)
            # si se demora más de 4 minutos se detiene la ejecuión y se lanza una Exception
            if 'is already running' in e.args[1]: #
                cnxn, cursor = get_db()
                running_execution_time = 0
                while running_execution_time <= 4:
                    load_execution_dates = cursor.execute("""
                    SELECT 
                    start_execution_date,
                    stop_execution_date
                    From msdb.dbo.sysjobactivity as ja
                    INNER JOIN msdb.dbo.sysjobs as j on j.job_id = ja.job_id
                    WHERE j.name = 'JobIndicadoresSIE'
                    AND start_execution_date IS NOT NULL
                    """).fetchall()

                    load_execution_dates.sort(key = lambda x: x[0])
                    load_execution_dates = load_execution_dates[-1]
                    ## En este caso load_execution_dates
                    # reotrna la última tupla que contiene la fecha de inicio del job
                    # y la fecha de final
                    # se espera que la fecha final sea nula para capturar el error de tipo 1
                    # si no es nula entonces algo extraño pasó
                    if load_execution_dates[1] != None:
                        cursor.close()
                        cnxn.close()
                        raise Exception("Error inesperado")
                    else:
                        start_execution_date = pd.to_datetime(load_execution_dates[0])
                        now_date = pd.to_datetime(datetime.datetime.now())
                        running_execution_time = pd.Timedelta(start_execution_date - now_date).seconds / 3600.0
                        
                        if running_execution_time > 4:
                            cursor.execute("EXEC msdb.dbo.sp_stop_job 'JobIndicadoresSIE' ")
                            cursor.close()
                            cnxn.close()
                            raise Exception(f"""
                            El job tardó {running_execution_time} minutos más de lo esperado
                            ----------------------------------------------------------------
                            
                            Se forzó la detención del job
                            """)

                cursor.close()
                cnxn.close()
            else:
                cursor.close()
                cnxn.close()
                raise Exception(e.args)

        ### ----------------------------------------------------------------
        # verificamos que no hayan errores
        
    else:
        return True








