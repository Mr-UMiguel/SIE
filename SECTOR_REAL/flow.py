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

    ## Si el rango existe y la conexión existe entonces
    # para metrizamos una condición para ejecutar o no ejecutar el job en SQL
    # update_state=0 No actualizar
    # update_state=1 Nuevas observaciones
    # update_state=2 Observaciones actuales actualizadas (actualización hacia atrás)
    update_state = 0

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

        if len(rows_db) != len(rows_macro):
            update_state = 1
        else:
            ## Comparamos los úlitmos 4 elementos ya que en series trimestres sería un año
            # y en series mensuales serían 4 meses
            # si son diferentes a los valores en base entonces se actualiza toda la serie 
            for rd,rm in zip(rows_db[-4:],rows_macro[-4:]):
                if rd != rm:
                    update_state = 2
                    break

        # Cerramos la macro y la conexión a Excel
        wb.close()
        xl_app.quit()
    else:
        raise Exception("File has not been compiled by Excel Macro or database connection doesn't exist")

    cursor.close()
    cnxn.close()
    
    return update_state



# @task(log_stdout=True)
def Load(update_state:str, refAreaID:str, flarID:str):
    cnxn, cursor = get_db()

    cursor.execute(
    """
    UPDATE [SIEDB].[dbo].[parametros]
    SET STATUS='2'
    """
    )
    ## Si el update_state != 0 entonces ejecutamos el job en la base de datos
    load_state = False
    if update_state != 0:
        # Cambiamos los parámetros
        cursor.execute("""
        UPDATE [SIEDB].[dbo].[parametros]
        SET STATUS=1
        WHERE country IN (?)
        AND fileName = (?)
        """, refAreaID, f"{flarID}.xlsm"
        )

        # Verificamos el codigo de ejecución
        verification_code = cursor.execute("""SELECT MAX(code) FROM [SIEDB].[dbo].[audit]""").fetchone()[0]

        # Ejecutamos el job
        print("""
        Iniciando la ejecución del job
        ********************************
        """)

        # cursor.execute("""
        # EXEC msdb.dbo.sp_stop_job ?
        # """, 'JobIndicadoresSIE')

        cursor.execute("""
        EXEC msdb.dbo.sp_start_job ?
        """, 'JobIndicadoresSIE')


        # load_state = cursor.fetchall()
        # load_state = pd.read_sql("""
        # EXEC msdb.dbo.sysjobhistory 
        #     @job_name = N'JobIndicadoresSIE'
        
        # """, cnxn)
        

        time.sleep(10)
        excecute_code = cursor.execute("""SELECT MAX(code) FROM [SIEDB].[dbo].[audit]""").fetchone()[0]
    
        print(verification_code, excecute_code)
        
        cursor.close()
        cnxn.close()
        if int(excecute_code) == int(verification_code) + 1:
            pass
            
            # job_response = cursor.execute("""
            # SELECT * FROM [SIEDB].[dbo].[audit]
            # WHERE code = ?
            # """, excecute_code).fetchall()
            
            # time_out = 0
            # while len(job_response) < 12:
            #     time.sleep(20)
            #     time_out += 20
            #     job_response = cursor.execute("""
            #     SELECT * FROM [SIEDB].[dbo].[audit]
            #     WHERE code = ?
            #     """, excecute_code).fetchall()

            #     ## Error de tipo 1
            #     ## Ocurrió un error al ejecutar el job

            #     err_1 = [i for i in job_response if i[3].find("Error") == 0 ]
            #     if (len(err_1) != 0):
            #         raise Exception(err_1[0]) 
                
            #     ## Error de tipo 2
            #     ## El job tardó más de lo esperado
            #     elif time_out == 60:
            #         raise Exception(f"El job tardó {time_out} segundos más de lo esperado")

            # if len(job_response) == 12:
            #     load_state = True
            
        else:
            raise Exception(f"El servidor SQL no ejecutó el job correspondiente al flujo de {flarID} - {refAreaID}")
    # Cerramos la conexión a la base de datos 
    # cursor.close()
    # cnxn.close()

    load_state.to_excel('D:/Desktop/load_state.xlsx')
    return load_state

# l = Load(update_state=2, refAreaID='AR', flarID='1.01.1')
# print(l)


# try:
#     cnxn, cursor = get_db()
#     print("""
#     Iniciando la ejecución del job
#     ------------------------------
#     """)
#     cursor.execute("EXEC msdb.dbo.sp_start_job 'JobIndicadoresSIE'")
#     cursor.close()
#     cnxn.close()
# except Exception as e:
#     cnxn, cursor = get_db()
#     if 'is already running' in e.args[1]:
#         running_execution_time = 0
#         while running_execution_time < 1:
#             load_execution_dates = cursor.execute("""
            # SELECT 
            # start_execution_date,
            # stop_execution_date
            # From msdb.dbo.sysjobactivity as ja
            # LEFT JOIN msdb.dbo.sysjobs as j on j.job_id = ja.job_id
            # WHERE j.name = 'JobIndicadoresSIE'
            # AND ja.start_execution_date IS NOT NULL
#             """).fetchall()
#             start_execution_date = pd.to_datetime(load_execution_dates[0][0])
#             now_date = pd.to_datetime(datetime.datetime.now())
#             running_execution_time = pd.Timedelta(start_execution_date - now_date).seconds / 3600.0
#             print(load_execution_dates)
#             if running_execution_time > 4:
#                 cursor.execute("EXEC msdb.dbo.sp_stop_job 'JobIndicadoresSIE' ")
#                 raise Exception(f"""
#                 El job tardó {running_execution_time} minutos más de lo esperado
#                 ----------------------------------------------------------------
                
#                 Se forzó la detención del job
#                 """)

#     cursor.close()
#     cnxn.close()




cnxn, cursor = get_db()
cursor.execute("EXEC msdb.dbo.sp_stop_job 'JobIndicadoresSIE' ")
load_status = pd.read_sql("""
SELECT 
*
From msdb.dbo.sysjobhistory as jh
LEFT JOIN msdb.dbo.sysjobs as j on j.job_id = jh.job_id
WHERE j.name = 'JobIndicadoresSIE'
""",cnxn).iloc[-1,:]

print(load_status)
cursor.close()
cnxn.close()

### Verificar el while
# pues siempre se deja ejecutando el job



