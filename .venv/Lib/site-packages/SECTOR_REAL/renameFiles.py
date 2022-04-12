import pandas as pd 
import numpy as np 
import sys , traceback, os ,shutil
from prefect import task


@task
def rename_and_save(filepath,filename,flar_name):
    shutil.move(f"{filepath}/{filename}",f"{filepath}/{flar_name}")
    print("File has been renamed and saved in {}".format(filepath + "/" + flar_name))

@task
def open_and_save(filepath,filename,flar_name,sheet_name=None):
    if sheet_name is not None:
        try:
            data = pd.read_excel(f"{filepath}/{filename}", sheet_name=sheet_name)
            data.to_csv(f"{filepath}/{flar_name}",encoding='latin1',sep=',',decimal='.')
            os.remove(f"{filepath}/{filename}")
            print("File has been renamed and saved in {}".format(filepath + "/" + flar_name))
        except Exception as e:
            print(f"""
            ----
            Error
            ----
            ubicación y archivo: {filepath + "/" + filename}
            tipo: {type(e).__name__}
            -----
            Información del error:
            -----
            + {e} 
            -----
            Posibles causas:
            -----
            1. el archivo no se descargo correctamente
            2. no se encontró la hoja en el archivo para ser
                guardada como csv, puede que esté mal escrita o
                que el archivo haya sido modificado por la fuente 
            """)

# class Rename():

#     def __init__(self,filepath,filename):
#         self.filename = filename
#         self.filepath = filepath

#     @task
#     def rename_and_save(self,flar_name):
#         shutil.move(f"{self.filepath}/{self.filename}",f"{self.filepath}/{flar_name}")
#         print("File has been renamed and saved in {}".format(self.filepath + "/" + flar_name))

#     @task
#     def open_and_save(self,flar_name,sheet_name=None):
#         if sheet_name is not None:
#             try:
#                 data = pd.read_excel(f"{self.filepath}/{self.filename}", sheet_name=sheet_name)
#                 data.to_csv(f"{self.filepath}/{flar_name}",encoding='latin1',sep=',',decimal='.')
#                 os.remove(f"{self.filepath}/{self.filename}")
#                 print("File has been renamed and saved in {}".format(self.filepath + "/" + flar_name))
#             except Exception as e:
#                 print(f"""
#                 ----
#                 Error
#                 ----
#                 ubicación y archivo: {self.filepath + "/" + self.filename}
#                 tipo: {type(e).__name__}
#                 -----
#                 Información del error:
#                 -----
#                 + {e} 
#                 -----
#                 Posibles causas:
#                 -----
#                 1. el archivo no se descargo correctamente
#                 2. no se encontró la hoja en el archivo para ser
#                    guardada como csv, puede que esté mal escrita o
#                    que el archivo haya sido modificado por la fuente 
#                 """)