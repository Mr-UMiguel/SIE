import pandas as pd 
import json

from ARG.db import get_db

settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']
file_path = "/TRANSFORM-DB/ARG"

def upload():
    cnxn , cursor = get_db()
    tables = [table.table_name for table in cursor.tables()]

    if 'pib' not in tables:
        ## Create table countries
        PIB_table = """
            CREATE TABLE pib (
                Date  DATETIME NOT NULL,
                Obsvalue DECIMAL NOT NULL,
            );
        """
        with cursor.execute(PIB_table):
            print("pib table has been created in")

    ## Delete all observations
    cursor.execute("DELETE FROM pib")

    # Load data
    data = pd.read_csv(root_path+file_path+"/1.01.1.csv")
    data.columns = ["Date","Obsvalue"]
    data["Date"] = pd.to_datetime(data["Date"])

    for date,obsvalue in zip(data["Date"],data["Obsvalue"]):
        sql_update = """
            INSERT INTO pib (Date, Obsvalue) VALUES(?,?)
        """
        cursor.execute(sql_update, date, obsvalue)
        cnxn.commit()

    cursor.close()
    cnxn.close()