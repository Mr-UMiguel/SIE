
from playwright.sync_api import Playwright, sync_playwright
from ARG.extract import run
from ARG.transform import clean
from ARG.load import upload


from prefect import task, Flow

@task #decorador de prefect 
def extract(log_stdout=True):
    print("""
    *******************************************************
            INICIANDO LA DESCARGA DE ARG
    """)
    with sync_playwright() as playwright:
        run(playwright)

@task
def transform(log_stdout=True):
    print("""
    *******************************************************
            INICIANDO LA LIMPIEZA DE ARG
    """)
    clean()

@task
def load(lof_stdout=True):
    print("""
    *******************************************************
            INICIANDO LA CARGA DE ARG
    """)
    upload()


with Flow("Extract PIB ARG") as flow:
    extract()
    transform()
    load()


flow.register(project_name="FLAR prueba")
# flow.run()