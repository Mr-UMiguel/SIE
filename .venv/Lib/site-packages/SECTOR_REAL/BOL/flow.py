from datetime import timedelta 
from prefect import task, Flow, Parameter 
import json
import sys

# from extract import *
# from transform import *
from SECTOR_REAL.BOL.extract import *
from SECTOR_REAL.renameFiles import *


settings = json.load(open('./settings.json','r'))
root_path = settings['root_path']


@task
def transform(fpath,rename_this_files):

    file_names = [i[0] for i in rename_this_files]
    new_names  = [i[1] for i in rename_this_files]
    for oname,nname in zip(file_names,new_names):
        if nname != '1_17_1.csv':
            r = rename_and_save(filepath=fpath,filename=oname,flar_name=nname)
        else:
            sheetName = Parameter('sheetName',default='CUADRO Nº 1.1 ÍNDICE MENSUAL')
            r = open_and_save(filepath=fpath,filename=oname,flar_name=nname, sheet_name=sheetName)

def bolFlow():
    with Flow('SECTOR_REAL-BOL') as flow:
        
        # Extraction tasks
        # fn is filename
        download_path  = Parameter('download_path', default=root_path+'/EXTRACT/SECTOR_REAL/BOL')
        fn1_01_1 = e1_01_1v(download_path=download_path)
        fn1_11_1 = e1_11_1v(download_path=download_path)
        fn1_17_1 = e1_17_1(download_path=download_path)

        ## Rename following files
        rename_tuples = [
            (fn1_01_1, '1_01_1.xlsx'),
            (fn1_11_1, '1_11-12_1.xlsx'),
            (fn1_17_1, '1_17_1.csv')
            ]
        transform(fpath=download_path,rename_this_files=rename_tuples)

    flow.register(project_name="FLAR prueba")