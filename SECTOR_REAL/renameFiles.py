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

