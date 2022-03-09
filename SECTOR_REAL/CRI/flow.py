from datetime import timedelta 
from prefect import task, Flow, Parameter 
import json
import sys

# from extract import *
# from transform import *
from SECTOR_REAL.CRI.extract import *
# from SECTOR_REAL.ARG.transform  import clea

settings = json.load(open('./settings.json','r'))
root_path = settings['root_path']

def criFlow():
        with Flow('SECTOR_REAL-CRI') as flow:
                # Extraction tasks
                # fn is filename
                download_path  = Parameter('download_path', default=root_path+'/EXTRACT/SECTOR_REAL/CRI')
                fn1_01_1 = e1_01_1(download_path=download_path)
                fn1_11_1 = e1_11_1(download_path=download_path)
                fn1_17_1 = e1_17_1(download_path=download_path)
        flow.register(project_name="FLAR prueba")
