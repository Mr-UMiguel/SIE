## Módulos propios
from SECTOR_REAL.db import get_db
from SECTOR_REAL.runMacro import run_excel_macro

# Prefect.io modules
from prefect import task

# Other modules
import datetime
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
    cnxn = None
    cnxn, cursor = get_db()

    ## Si el rango existe y la conexión existe entonces
    # para metrizamos una condición para ejecutar o no ejecutar el job en SQL
    # update_state=0 No actualizar
    # update_state=1 Nuevas observaciones
    # update_state=2 Observaciones actuales actualizadas (actualización hacia atrás)
    update_state = 0

    if rango != None and cnxn != None:
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
    if cnxn != None:
        cursor.execute(
        """
        UPDATE [SIEDB].[dbo].[parametros]
        SET STATUS=2
        """
        )
        ## Si el update_state != 0 entonces ejecutamos el job en la base de datos
        if update_state != 0:
            # Cambiamos los parámetros
            # cursor.execute("""
            # UPDATE [SIEDB].[dbo].[parametros]
            # SET STATUS=1
            # WHERE country IN (?)
            # AND fileName = (?)
            # """, refAreaID, f"{flarID}.xlsm"
            # )

            # Ejecuto el job

            # Verificamos el log
            load_status = None

            cursor.execute(
            """
            select * from [SIEDB].[dbo].[audit]
            where code = (select max(code) from [SIEDB].[dbo].[audit] )
            """
            )

            r = cursor.fetchall()
            if len(r) != 12:
                pass

Load(update_state=2, refAreaID='AR', flarID='1.01.1')