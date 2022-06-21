
import xlwings as xw

def run_excel_macro(file_path):
    """
    Execute an Excel macro
    :param file_path: path to the Excel file holding the macro
    :return: None
    """
    xl_app = xw.App(visible=False, add_book=False)
    wb = xl_app.books.open(file_path)
    rango = None
    try:
        ### Ejectuamos la macro
        run_macro = wb.app.macro('cargue')
        run_macro()
        # ### Checamos la data
        sheet = wb.sheets[0]
        table = sheet.tables[0]
        rango = table.range.end('down').get_address().split('$')[2]
        
        wb.save(file_path)
        ### cerramos el archivo y la conexión
        wb.close()  
        xl_app.quit()
        

    except Exception as ex:
        wb.close()  
        xl_app.quit()
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

    return rango

