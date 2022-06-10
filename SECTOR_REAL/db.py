import pyodbc
from prefect.tasks.secrets import PrefectSecret

def get_db():
    server = 'FLAR-TSQL2017\TSQL2017'
    database = 'SIEDB'
    username = 'sql_dee'
    password = 'QbB^~lpkLUIcA|r'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    cursor = cnxn.cursor()

    return cnxn, cursor    

