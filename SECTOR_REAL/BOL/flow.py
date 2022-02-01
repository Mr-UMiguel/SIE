from datetime import timedelta 
from prefect import task, Flow, Parameter 
import json
import sys

from extract import *
from transform import *
# from SECTOR_REAL.ARG.extract import *
# from SECTOR_REAL.ARG.transform  import clean

from playwright.sync_api import sync_playwright



settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']

# 
@task(log_stdout=True)
def extract_1_01_1():
    print("""
    ****************************************
    Iniciando la extracción de 1_01_1 en ARG
    ****************************************
    """)

    with sync_playwright() as playwright:
        filename =  e1_01_1(playwright,download_path=root_path+"/EXTRACT/SECTOR_REAL/BOL")

    return filename

@task
def extract_1_11_1():
    print("""
    ****************************************
    Iniciando la extracción de 1_11_1 en ARG
    ****************************************
    """)
    with sync_playwright() as playwright:
            filename =  e1_11_1(playwright,download_path=root_path+"/EXTRACT/SECTOR_REAL/BOL")

    return filename



# @task(log_stdout=True,)
# def transform_1_01_1(filename):
#     print("""
#     ********************************************
#     Iniciando la transformación de 1_11_1 en ARG
#     ********************************************
#     """)
#     clean_1_01_1(filename,
#                 extract_path=root_path+"/EXTRACT/SECTOR_REAL/ARG",
#                 save_path=root_path+'/TRANSFORM/SECTOR_REAL/ARG')


with Flow("ARG") as flow:
    
    # Extraction tasks
    # fn1_01_1 = extract_1_01_1()
    fn1_11_1 = extract_1_11_1()

    # Transform tasks
    # transform_1_01_1(filename=fn1_01_1)
    

# flow.register(project_name="FLAR prueba")
flow.run()