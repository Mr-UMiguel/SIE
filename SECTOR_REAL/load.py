import pandas as pd
import numpy as np
from SECTOR_REAL.db import get_db, create_table_pib
import json

settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']
file_path = "/TRANSFORM-DB/"

def upload():
    cnxn, cursor = get_db()
    
    tables = [table.table_name for table in cursor.tables()]

    if 'pib' not in tables:
        create_table_pib()
    
        

    data = pd.DataFrame({})
    for i in ["ARG","CHL","COL"]:
        try:
            data_temp = pd.read_csv(root_path+file_path+i+'/1.01.1.csv',decimal='.')
            data_temp.columns = ["Date",i]
            data_temp.set_index("Date",drop=True,inplace=True)
        except:
            data_temp = 0
        
        data = pd.concat([data,data_temp],axis="columns")

    data = data.fillna(0)
    print(data)
    cursor.execute("DELETE FROM pib")

    for date,arg,chl,col in zip(data.index,
    data["ARG"],data['CHL'],data['COL']):
        sql_update = """
            INSERT INTO pib (Date, ARG,CHL, COL) VALUES(?,?,?,?)
        """
        cursor.execute(sql_update, date, arg, chl, col)
        cnxn.commit()

    cursor.close()
    cnxn.close()
