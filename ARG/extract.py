import pandas as pd
import numpy as np 
import requests
from bs4 import BeautifulSoup
import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']


def run(playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://www.indec.gob.ar/
    page.goto("https://www.indec.gob.ar")
    # Click text=ESTADÍSTICAS
    page.click("text=ESTADÍSTICAS")
    # Click text=Cuentas nacionales
    # with page.expect_navigation(url="https://www.indec.gob.ar/indec/web/Nivel3-Tema-3-9"):
    with page.expect_navigation(url="https://www.indec.gob.ar/indec/web/Nivel3-Tema-3-9"):
        page.click("text=Cuentas nacionales")
    # Click text=Agregados macroeconómicos (PIB)
    page.click("text=Agregados macroeconómicos (PIB)")
    # 0× click
    # page.click("text=Agregados macroeconómicos (PIB)")
    # assert page.url == "https://www.indec.gob.ar/indec/web/Nivel4-Tema-3-9-47"
    # Click #contenidoPrincipal >> :nth-match(div:has-text("PIB Ingreso y ahorro nacional Formación bruta de capital fijo Producto interno b"), 2)
    page.click("#contenidoPrincipal >> :nth-match(div:has-text(\"PIB Ingreso y ahorro nacional Formación bruta de capital fijo Producto interno b\"), 2)")
    

    with page.expect_download() as download_info:
        page.locator('//*[@id="1"]/div[2]/div[1]/div[2]/div/div/a').click()
    download = download_info.value
    download.save_as(root_path+f"/EXTRACT-DB/ARG/{download.suggested_filename}")
    # with page.expect_download() as download_info:
    #     with page.expect_popup() as popup_info:
    #         page.click("text=Series trimestrales de oferta y demanda globales. Años 2004-2021")
    #     page1 = popup_info.value
    # download = download_info.value
    # download.save_as("D:/Documents/Miguel/FLAR/SIE/EXTRACT/ARG/DATA-BASES/REAL-SECTOR/{}".format(download.suggested_filename))

    url = page.url
    content = page.locator('//*[@id="1"]/div[2]/div[1]/div[2]/div/div/a').text_content()

    print(f"""
    **********************************
    {url}
    ----------------------------------
    {content}
    File has been successfully downloaded 
    {root_path+f"/EXTRACT-DB/ARG/{download.suggested_filename}"}
    """)
    # ---------------------
    context.close()
    browser.close()
    
