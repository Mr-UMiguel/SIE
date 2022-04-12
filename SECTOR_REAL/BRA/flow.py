from prefect import task, Flow, Parameter 
import json, shutil, os

# from extract import *
# from transform import *
from SECTOR_REAL.BRA.extract import *
from SECTOR_REAL.renameFiles import *


settings = json.load(open('./settings.json','r'))
root_path = settings['root_path']

@task
def transform(fpath,rename_this_files):


    file_names = [i[0] for i in rename_this_files]
    new_names  = [i[1] for i in rename_this_files]
    for oname,nname in zip(file_names,new_names):
        if nname not in ['1_11_1.csv','1_01-02-03-04-05-06-07-09_1.xls']:
            r = rename_and_save(filepath=fpath,filename=oname,flar_name=nname)
        elif nname == '1_11_1.csv':
            sheetName = Parameter('sheetName',default=0)
            r = open_and_save(filepath=fpath,filename=oname,flar_name=nname, sheet_name=sheetName)
        elif nname== '1_01-02-03-04-05-06-07-09_1.xls':
            try:
                shutil.unpack_archive(f'{fpath}/{oname}',f'{fpath}/{nname}')
                shutil.move(f'{fpath}/{nname}/{oname}',f'{fpath}/{nname}')
            except Exception as e:
                print(f"""
                Ocurrió un error al descomprimir el archivo {oname}, 
                Corresponiendte al {nname} de Brasil

                Error:
                --------------------------------
                {type(e).__name__}
                """)

def braFlow():
    with Flow('SECTOR_REAL-BRA') as flow:
        
        # Extraction tasks
        # fn is filename
        download_path  = Parameter('download_path', default=root_path+'/EXTRACT/SECTOR_REAL/BRA')
        fn1_01_1 = e1_01_1(download_path=download_path)
        fn1_11_1 = e1_11_1(download_path=download_path)
        fn1_17_1 = e1_17_1(download_path=download_path)

        ## Rename following files
        rename_tuples = [
            (fn1_01_1, '1_01-02-03-04-05-06-07-09_1.xls'),
            (fn1_11_1, '1_11_1.csv'),
            (fn1_17_1, '1_17_1.xlsx')
            ]
        transform(fpath=download_path,rename_this_files=rename_tuples)

    flow.register(project_name="FLAR prueba")
