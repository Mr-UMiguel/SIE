import pandas as pd 
import numpy as np 
import json
import os

settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']
file_path = "/EXTRACT-DB/CHL"
# file_name = os.listdir(root_path+file_path)[0]
# file_name = "Cuadro_24012022131949.xlsx"

def clean(filename):
    df = pd.read_excel(root_path+file_path+f"/{filename}")
    pib = pd.DataFrame(df.iloc[2:,2])
    pib.columns = ["CHL"]
    date_range = pd.date_range('30-01-2015',freq="Q",periods=len(pib))
    pib.set_index(date_range,drop=True,inplace=True)
    pib = pib.pct_change(4)*100
    pib = pib.round(2)
    pib.to_csv(root_path+"/TRANSFORM-DB/CHL/1.01.1.csv", decimal=',')
