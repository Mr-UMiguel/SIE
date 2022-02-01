import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']

series = json.load(open("./series.json","r"))['SECTOR_REAL']['PER']


def e1_01_1(playwright, download_path) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(accept_downloads=True)

    # Open new page
    page = context.new_page()
    
    #go to
    page.goto('https://www.inei.gob.pe/estadisticas/indice-tematico/economia')

    with page.expect_download() as download_info:
        page.locator('//*[@id="contenido"]/ul/li[2]/ul/li/ul/li[1]/ul/li[1]/a').click()
    download = download_info.value

    url = page.url
    content = page.locator('//*[@id="contenido"]/ul/li[2]/ul/li/ul/li[1]/ul/li[1]/a').text_content()
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
    page.goto(hrefDynamic[0])

    # page.goto("https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN38063GM/html")
    # Click input[name="btnExportacionXls"]
    with page.expect_download() as download_info:
        page.click('input[name=\"btnExportacionXls\"]')
    download = download_info.value
    # Close page


    url = page.url
    content = page.locator('//*[@id="frmMensual"]/h1').text_content()


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

