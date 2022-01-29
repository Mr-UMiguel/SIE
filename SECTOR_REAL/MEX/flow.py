from playwright.sync_api import Playwright, sync_playwright
from extract import run

from prefect import task, Flow

# @task #decorador de prefect 
def extract(log_stdout=True):
    print("""
    ********************************************
            INICIANDO LA DESCARGA DE MEX
    """)
    with sync_playwright() as playwright:
        run(playwright)

extract()