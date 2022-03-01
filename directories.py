import os 
import json


def create_directories(storage_path):
    cwd = os.listdir(storage_path)

    # CERPETAS DE LAS TAREAS EXTRACCIÓN Y TRANSFORMACIÓN

    extract =  "EXTRACT"
    transform = "TRANSFORM" 
    if  extract not in cwd:
        os.mkdir(storage_path+f"/{extract}")
        
    if  transform not in cwd:
        os.mkdir(storage_path+f"/{transform}") 

    # CARPETAS DE LOS SECTORES
    ewd = os.listdir(storage_path+ f"/{extract}")
    twd = os.listdir(storage_path+ f"/{transform}")

    real_sector = "SECTOR_REAL"
    financial_sector = "SECTOR_FINANCIERO"
    external_sector = "SECTOR_EXTERNO"
    fiscal_sector = "SECTOR_FISCAL"

    if  real_sector not in ewd or  real_sector not in twd:
        os.mkdir(storage_path+ f"/{extract}"+f"/{real_sector}")
        os.mkdir(storage_path+ f"/{transform}"+f"/{real_sector}")
    if  financial_sector not in ewd or  financial_sector not in twd:
        os.mkdir(storage_path+ f"/{extract}"+f"/{financial_sector}")
        os.mkdir(storage_path+ f"/{transform}"+f"/{financial_sector}")
    if  external_sector not in ewd or  external_sector not in twd:
        os.mkdir(storage_path+ f"/{extract}"+f"/{external_sector}")
        os.mkdir(storage_path+ f"/{transform}"+f"/{external_sector}")
    if  fiscal_sector not in ewd or  fiscal_sector not in twd:
        os.mkdir(storage_path+ f"/{extract}"+f"/{fiscal_sector}")
        os.mkdir(storage_path+ f"/{transform}"+f"/{fiscal_sector}")
    


    # CARPETAS DE LOS PAISES
    try:
        countries = json.load(open("./countries.json","r"))
        countryID = [i['countryID'] for i in countries]
    except:
        print("Proporcione un archivo Json con las carecterísitcas de los países")

    for sector in os.listdir(storage_path+f'/{extract}'):
        for country in countryID:
            try:
                os.mkdir(storage_path+ f"/{extract}/{sector}/{country}")
            except:
                pass

    for sector in os.listdir(storage_path+f'/{transform}'):
        for country in countryID:
            try:
                os.mkdir(storage_path+ f"/{transform}/{sector}/{country}")
            except:
                pass
    
    
create_directories("D:/Desktop")