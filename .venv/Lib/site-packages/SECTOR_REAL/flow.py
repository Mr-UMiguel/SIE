from prefect import Task, Flow, Parameter, task
from SECTOR_REAL.db import get_db
from SECTOR_REAL.runMacro import run_excel_macro
import datetime
import xlwings as xw


@task(log_stdout=True, max_retries=1,retry_delay=datetime.timedelta(seconds=10),)
def Extract(function, download_path:str):
    r = function(download_path)
    return r

@task(log_stdout=True)
def Transform(function,file_name:str,flar_name:str,
            download_path:str,file_macro:str,refAreaID:str,flarID:str):

    ### Renombramos el archivo 
    state = function(file_name,flar_name,download_path)
    if state == True:
        rango = run_excel_macro(file_macro)

    cnxn = None
    ## Creamos la conexión a la base de datos
    cnxn, cursor = get_db()

    if rango != None and cnxn != None:
        ### Creamos la conexión y abrimos la macro 
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

        cursor.execute(
                    """
            SELECT timePeriod, obsValue FROM observation_value 
            WHERE observation_value.serieID = ?
            """, serieID
        )

        ### Validamos la información
        ## Nuevos datos
        rows_db = cursor.fetchall()
        rows_macro = ws.range(f"A11:B{rango}").options(ndim=2).value

        if len(rows_db) == len(rows_macro):
            for rd,rm in zip(rows_db,rows_macro):
                print(rd,rm)

        wb.close()
        xl_app.quit()
    else:
        raise Exception("File has not been compiled by Excel Macro")

    cursor.close()
    cnxn.close()
    
    return rango

@task(log_stdout=True)
def Load():
    pass


