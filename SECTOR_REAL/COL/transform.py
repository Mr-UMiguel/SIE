import pandas as pd 
import numpy as np 
import json
import os

settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']
file_path = "/EXTRACT-DB/COL"
# file_name = os.listdir(root_path+file_path)[0]

def clean(filename):
    df = pd.read_excel(root_path+file_path+f"/{filename}", sheet_name="Cuadro 1")
    pib = pd.DataFrame(df.iloc[27,3:])
    pib.columns = ['COL']
    date_range = pd.date_range('30-01-2005',freq="Q",periods=len(pib))
    pib.set_index(date_range, drop=True,inplace=True)
    pib = pib.pct_change(4)*100
    pib = pib.round(2)
    pib.to_csv(root_path+"/TRANSFORM-DB/COL/1.01.1.csv", decimal=',')

