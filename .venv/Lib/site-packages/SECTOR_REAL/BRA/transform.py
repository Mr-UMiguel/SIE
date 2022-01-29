import pandas as pd 
import numpy as np 
import json
import os
import shutil

settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']
file_path = "/EXTRACT-DB/BRA"
# filename = 'Tab_Compl_CNT.xls'
def clean(filename):
    shutil.unpack_archive(root_path+file_path+f"/{filename}",root_path+file_path)
    os.remove(root_path+file_path+f"/{filename}")
    filename_ = os.listdir(root_path+file_path)[0]    
    df = pd.read_excel(root_path+file_path+f"/{filename_}",
                       sheet_name='Valores Encadeados a Preços 95')
    pib = pd.DataFrame(df.iloc[3:,17]).applymap(lambda x: float(x))
    pib.columns = ['BRA']
    date_range = pd.date_range('30-01-1996',freq="Q",periods=len(pib))
    pib = pib.set_index(date_range,drop=True) 
    pib = pib.pct_change(4)*100

    pib.to_csv(root_path+"/TRANSFORM-DB/BRA/1.01.1.csv",decimal=',')


