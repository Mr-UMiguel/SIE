import pyodbc

def get_db():
    server = 'DESKTOP-86PG3QV\SQLEXPRESS'
    database = 'pruebaDB'
    username = 'sa'
    password = 'GHJ_1357#'

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    cursor = cnxn.cursor()

    return cnxn, cursor    

def create_table_pib():
    cnxn , cursor = get_db()
    tables = [table.table_name for table in cursor.tables()]

    if 'pib' not in tables:
        ## Create table countries
        PIB_table = """
            CREATE TABLE pib (
                Date  DATETIME NOT NULL,
                ARG numeric(10,5) NULL,
                BOL numeric(10,5) NULL,
                BRA numeric(10,5) NULL,
                CHL numeric(10,5) NULL,
                COL numeric(10,5) NULL,
            );
        """
        with cursor.execute(PIB_table):
            print("PIB table has been created in")

    cursor.close()
    cnxn.close()
