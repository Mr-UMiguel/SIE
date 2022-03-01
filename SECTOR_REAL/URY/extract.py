import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']

series = json.load(open("./series.json","r"))['SECTOR_REAL']['URY']

def e1_01_1(playwright, download_path) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(accept_downloads=True)

    # Open new page
    page = context.new_page()

    # Go to https://bcn.gob.ni/cuentas-nacionales-trimestrales
    page.goto("https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Paginas/Series-Estadisticas-del-PIB-por-industrias.aspx")

    with page.expect_download() as download_info:
        page.locator('//*[@id="ctl00_ctl63_g_00ff9073_4c37_41a1_aebe_602a00cad5ce_ctl00_documents"]/tbody/tr[1]/td[8]/a').click()
    download = download_info.value


    url = page.url
    content = page.locator('//*[@id="ctl00_ctl63_g_00ff9073_4c37_41a1_aebe_602a00cad5ce_ctl00_documents"]/tbody/tr[1]/td[8]/a').text_content()
    #### PARA GUARDAR EL ARCHIVO ###########
    ### NO MODIFCAR ESTA PARTE 
    download.save_as(download_path+f"/{download.suggested_filename}")

    print(f"""
    **********************************
    {url}
    ----------------------------------
    {content}
    File has been successfully downloaded 
    {download_path+f"/{download.suggested_filename}"}
    """)
    # ---------------------
    context.close()
    browser.close()

    return download.suggested_filename

# 1.11.1 Desempleo

def e1_11_1(playwright,download_path) -> None:
    pass



from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    e1_01_1(playwright, download_path="D:/Documents/Miguel/FLAR/SIE/EXTRACT/SECTOR_REAL/URY")
    e1_11_1(playwright, download_path="D:/Documents/Miguel/FLAR/SIE/EXTRACT/SECTOR_REAL/URY")