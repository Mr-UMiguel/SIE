import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']

series = json.load(open("./series.json","r"))['SECTOR_REAL']['MEX']


def e1_01_1(playwright, download_path) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(accept_downloads=True)

    # Open new page
    page = context.new_page()

    # Go to https://www.inegi.org.mx/temas/pib/
    page.goto("https://www.inegi.org.mx/temas/pib/")

    # 0× click
    page.click("html")
    # assert page.url == "https://www.inegi.org.mx/temas/pib/#Herramientas"

    # Click text=Tabulados
    page.click("text=Tabulados")
    # assert page.url == "https://www.inegi.org.mx/temas/pib/#Tabulados"

    # Click text=Series originales
    page.click("text=Series originales")

    # Click text=Serie detallada
    page.click("text=Serie detallada")

    # Click text=Valores constantes a precios de 2013
    page.click("text=Valores constantes a precios de 2013")

    # Click [aria-label="Descarga\ el\ archivo\ Millones\ de\ pesos\ a\ precios\ de\ 2013\ en\ formato\ xlsx"] img
    # with page.expect_navigation(url=":"):

    with page.expect_download() as download_info:
        page.click('//*[@id="tblDescargaArchivos_descargaMasiva"]/tbody/tr[7]/td[3]/div/a')
    download = download_info.value

    # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
    url = page.url
    content = page.locator('//*[@id="tblDescargaArchivos_descargaMasiva"]/tbody/tr[7]/td[3]/div/a').text_content()
    
    
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

    # go to  "https://gee.bccr.fi.cr/indicadoreseconomicos/Cuadros/frmVerCatCuadro.aspx?idioma=1&CodCuadro=%205504"
    hrefDynamic = [i['hrefDynamic'] for i in series if i['flarID']=="1.11.1"]
    page.goto(hrefDynamic[0])

    # Click #btn_tablagraf_gral0
    page.click("#btn_tablagraf_gral0")
    # Click #btn_exportaCSVgraf_gral0
    with page.expect_download() as download_info:
        page.click("#btn_exportaCSVgraf_gral0")
    download = download_info.value


    url = page.url
    content = page.locator('#btn_exportaCSVgraf_gral0').text_content()


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

