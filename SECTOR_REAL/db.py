import pyodbc
from prefect.client import Secret

def get_db():
    server = 'FLAR-TSQL2017\TSQL2017'
    database = 'SIEDB'
    username = 'sql_dee'
    password = Secret("GHJ7516").get()
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    cursor = cnxn.cursor()

    return cnxn, cursor    

