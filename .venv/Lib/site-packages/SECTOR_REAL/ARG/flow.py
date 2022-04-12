from datetime import timedelta
from fileinput import filename 
from prefect import task, Flow, Parameter 
import json, sys, os

import pandas as pd

# from extract import *
# from transform import *
from SECTOR_REAL.ARG.extract import *
from SECTOR_REAL.renameFiles import *




settings = json.load(open('./settings.json','r'))
root_path = settings['root_path']


def transform(fpath,rename_this_files):
    file_names = [i[0] for i in rename_this_files]
    new_names  = [i[1] for i in rename_this_files]

    for oname,nname in zip(file_names,new_names):
        if nname != '1_17_1.csv':
            r = rename_and_save(filepath=fpath,filename=oname,flar_name=nname)
        else:
            sheetName = Parameter('sheetName',default='Índices aperturas')
            r = open_and_save(filepath=fpath,filename=oname,flar_name=nname, sheet_name=sheetName)
        


def argFlow():
    with Flow('SECTOR_REAL-ARG') as flow:
        
        # Extraction tasks
        # fn is filename
        download_path  = Parameter('download_path', default=root_path+'/EXTRACT/SECTOR_REAL/ARG')
        fn1_01_1 = e1_01_1v(download_path=download_path)
        fn1_11_1 = e1_11_1v(download_path=download_path)
        fn1_17_1 = e1_17_1(download_path=download_path)

        ## Rename following files
        rename_tuples = [
            (fn1_01_1, '1_01-02-03-04-05-06-07-08-09_1.xls'),
            (fn1_11_1, '1_11-12-13_1.xls'),
            (fn1_17_1, '1_17_1.csv')
            ]
        # open_and_save(flar_name='1_17_1.csv',sheet_name='Índices aperturas')
        transform(fpath=download_path,rename_this_files=rename_tuples)

    # flow.run()
    flow.register(project_name="FLAR prueba") 
