from datetime import timedelta 
from prefect import task, Flow, Parameter 
import json
import sys

# from extract import *
# from transform import *
from SECTOR_REAL.COL.extract import *
from SECTOR_REAL.renameFiles import *
# from SECTOR_REAL.ARG.transform  import clean

settings = json.load(open('./settings.json','r'))
root_path = settings['root_path']


def Rename(fpath,rename_this_files):
    file_names = [i[0] for i in rename_this_files]
    new_names  = [i[1] for i in rename_this_files]

    for oname,nname in zip(file_names,new_names):
        r = rename_and_save(filepath=fpath,filename=oname,flar_name=nname)


with Flow('SECTOR_REAL-COL') as flow:
    
    # Extraction tasks
    # fn is filename
    download_path  = Parameter('download_path', default=root_path+'/EXTRACT/SECTOR_REAL/COL')
    fn1_01_1 = e1_01_1v(download_path=download_path)
    fn1_11_1 = e1_11_1v(download_path=download_path)
    fn1_17_1 = e1_17_1(download_path=download_path)



    ## Rename following files
    # rename_tuples = [
    #     ('1.1.INF_Serie historica Meta de inflacion IQY.xlsx', '1_01_1.xlsx'),
    #     ('anexo_empleo_feb_22.xlsx', '1_11-12-13-14_1.xlsx'),
    #     ('Anexos_produccion_constantes_IV_2021.xlsx', '1_17_1.xlsx')
    #     ]
    rename_tuples = [
        (fn1_01_1, '1_01_1.xlsx'),
        (fn1_11_1, '1_11-12-13-14_1.xlsx'),
        (fn1_17_1, '1_17_1.xlsx')
        ]
    Rename(fpath=download_path,rename_this_files=rename_tuples)

# flow.run()
flow.register(project_name="FLAR prueba")
