import xlwings as xw
import sys , traceback, os ,shutil

def rename_and_save(file_name,flar_name,download_path):
    """
    Use esta función para renombrar archivos del tipo .xlsx a .xls o de .xls a .xlsx
    """
    state = False
    xl_app = xw.App(visible=False, add_book=False)
    try:
        wb = xl_app.books.open(download_path+f'/{file_name}')
        wb.save(download_path+f'/{flar_name}')
        wb.close()
        xl_app.quit()

        state = True
        os.remove(download_path+f'/{file_name}')
        print(f"""
        File has been successfully renamed and saved as
        ------------------------------------------------
        {download_path+f'/{flar_name}'}
        """)
    except:
        xl_app.quit()
        raise Exception(""""File failed to rename and saved""")


    return state

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