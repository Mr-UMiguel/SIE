import pandas as pd 
import numpy as np 
import json
import os

settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']
file_path = "/EXTRACT-DB/BOL"
# filename = '01.01.01.xlsx'
def clean(filename):
    df = pd.read_excel(root_path+file_path+f"/{filename}")

    pib = df.iloc[9:,15]
    pib = pib.reset_index(level=0,drop=True)
    new_pib = []
    for idx, i in enumerate(pib):
        if idx%5 != 0:
            new_pib.append(i)
    new_pib = pd.DataFrame(new_pib).dropna()
    new_pib.columns = ['BOL']

    date_range = pd.date_range(start='30-01-1990', freq = 'Q', periods = len(new_pib))
    new_pib = new_pib.set_index(date_range)
    new_pib = new_pib.pct_change(4)*100
    new_pib = new_pib.round(2)
    
    new_pib.to_csv(root_path+"/TRANSFORM-DB/BOL/1.01.1.csv", decimal=',')
