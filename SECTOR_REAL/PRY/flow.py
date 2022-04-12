from datetime import timedelta 
from prefect import task, Flow, Parameter 
import json
import sys

# from extract import *
# from transform import *
from SECTOR_REAL.PRY.extract import *
# from SECTOR_REAL.ARG.transform  import clean


settings = json.load(open('./settings.json','r'))
root_path = settings['root_path']

def pryFlow():
        with Flow('SECTOR_REAL-PRY') as flow:
                # Extraction tasks
                # fn is filename
                download_path  = Parameter('download_path', default=root_path+'/EXTRACT/SECTOR_REAL/PRY')
                fn_base = base(download_path=download_path)
                fn1_01_1 = e1_11_1(download_path=download_path)

        flow.register(project_name="FLAR prueba")