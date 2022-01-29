import pyodbc

def get_db():
    server = 'DESKTOP-86PG3QV\SQLEXPRESS'
    database = 'pruebaDB'
    username = 'sa'
    password = 'GHJ_1357#'

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    cursor = cnxn.cursor()

    return cnxn, cursor    