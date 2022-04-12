from prefect import task, Flow, Parameter 
import json

# from extract import *
# from transform import *
from SECTOR_REAL.CHL.extract import *
from SECTOR_REAL.renameFiles import *

settings = json.load(open('./settings.json','r'))
root_path = settings['root_path']

@task
def transform(fpath,rename_this_files):

    file_names = [i[0] for i in rename_this_files]
    new_names  = [i[1] for i in rename_this_files]
    for oname,nname in zip(file_names,new_names):
        if nname not in ['1_01_1.csv','1_11-13_1.csv']:
            r = rename_and_save(filepath=fpath,filename=oname,flar_name=nname)
            
        else:
            sheetName = Parameter('sheetName',default=0)
            r = open_and_save(filepath=fpath,filename=oname,flar_name=nname, sheet_name=sheetName)

def chlFlow():
    with Flow('SECTOR_REAL-CHL') as flow:
        
        # Extraction tasks
        # fn is filename
        download_path  = Parameter('download_path', default=root_path+'/EXTRACT/SECTOR_REAL/CHL')
        fn1_01_1 = e1_01_1(download_path=download_path)
        fn1_11_1 = e1_11_1(download_path=download_path)
        fn1_17_1 = e1_17_1(download_path=download_path)

        ## Rename following files
        rename_tuples = [
            (fn1_01_1, '1_01_1.csv'),
            (fn1_11_1, '1_11-13_1.csv'),
            (fn1_17_1, '1_17_1.csv')
            ]
        transform(fpath=download_path,rename_this_files=rename_tuples)
    flow.register(project_name="FLAR prueba")