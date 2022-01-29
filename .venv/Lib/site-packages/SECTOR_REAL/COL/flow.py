from datetime import timedelta 
from prefect import task, Flow, Parameter 

from SECTOR_REAL.COL.extract import run
from SECTOR_REAL.COL.transform  import clean

from playwright.sync_api import Playwright, sync_playwright

@task(max_retries = 3, retry_delay = timedelta(seconds=20), log_stdout=True)
def extract():
    print("""
    **************************+
    Iniciando la descarga de COL
    """)
    with sync_playwright() as playwright:
        return run(playwright)

@task(log_stdout=True,)
def transform(filename):
    print("""
        Iniciando la transformación del PIB de COL
    """)
    return clean(filename)


with Flow("Extract 1.01.1 COL") as flow:
    filename = extract()
    transform(filename=filename)
    

flow.register(project_name="FLAR prueba")
# flow.run()