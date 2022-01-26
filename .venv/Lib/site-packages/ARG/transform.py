import pandas as pd 
import numpy as np 
import json
import os

settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']
file_path = "/EXTRACT-DB/ARG"
file_name = os.listdir(root_path+file_path)[0]

def clean():
    df = pd.read_excel(root_path+file_path+f"/{file_name}", sheet_name="cuadro 4")
    
    header = df.iloc[3,1:].dropna()
    total_mask = header.str.lower().str.contains("total")
    total_ci = header[total_mask].index #contiene los índices de las columnas que contienen "total" para ser eliminadas

    df_wo_total = df.drop(total_ci, axis=1)
    pib = df_wo_total.iloc[5,1:].dropna()/4 #argentina publica el pib acumulado anual, por ende cada trimestre se divide entre 4 
    pib = pib.dropna() #se eliminan los valores nulos

    date_range = pd.date_range(start="31/12/2003", freq="Q", periods=len(pib))
    if len(date_range) == len(pib):
        pib = pd.DataFrame(pib).applymap(lambda x: float(x)).set_index(date_range)
        pib.columns = ["Obsvalue"]
        pib = pib.pct_change(4) #Variación Anual 
        pib = pib.dropna().round(3)*100
        pib.to_csv(root_path+"/TRANSFORM-DB/ARG/1.01.1.csv")
    else:
        print("El rango de fecha no coincide con la longitud del indicador")
