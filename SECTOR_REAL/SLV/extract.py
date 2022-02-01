import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']

series = json.load(open("./series.json","r"))['SECTOR_REAL']['SLV']


def e1_01_1(playwright, download_path) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(accept_downloads=True)

    # Open new page
    page = context.new_page()

    # Go to https://bcn.gob.ni/cuentas-nacionales-trimestrales
    page.goto("https://www.bcr.gob.sv/bcrsite/?cat=1000&lang=es")

    # Locator
    page.locator('//*[@id="esq_43"]/div[2]/div[1]/a').click()

    # Locator
    page.locator('//*[@id="bcr_cuerpo"]/div[2]/form/div[4]/div[2]/div[4]/div[1]/div[1]/div/a').click()

    with page.expect_download() as download_info:
        page.locator('//*[@id="bcr_cuerpo"]/div[2]/form/div[5]/div[1]/div[2]/a').click()
    download = download_info.value


    url = page.url
    content = page.locator('//*[@id="bcr_cuerpo"]/div[2]/form/div[4]/div[2]/div[4]/div[1]/div[1]/div/a').text_content()
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
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    hrefDynamic = [ i['hrefDynamic'] for i in series if i['flarID']=="1.11.1"]

    page.goto('http://aplicaciones.digestyc.gob.sv/estadisticas.empleo/estadisticas_empleo/index.aspx')

    page.click("//html/body/div[2]/div[1]/div[1]/div[15]/img")


    with page.expect_download() as download_info:
        page.click('//*[@id="arbol_archivos"]/ul/li[8]/a')
    download = download_info.value

    url = page.url
    content = page.locator('//*[@id="arbol_archivos"]/ul/li[8]/a').text_content()


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

