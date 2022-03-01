from datetime import timedelta 
from prefect import task, Flow, Parameter 
import json
import sys

from extract import *
# from transform import *
# from SECTOR_REAL.ARG.extract import *
# from SECTOR_REAL.ARG.transform  import clean

from playwright.sync_api import sync_playwright



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
        flow.run()

criFlow()
 