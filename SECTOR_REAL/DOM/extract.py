import json
settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']

series = json.load(open("./series.json","r"))['SECTOR_REAL']['DOM']

def e1_01_1(playwright, download_path) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.bancentral.gov.do/
    page.goto("https://www.bancentral.gov.do/")

    # Click text=Estadísticas
    page.click("text=Estadísticas")

    # Click text=Sector Real
    page.click("text=Sector Real")
    # assert page.url == "https://www.bancentral.gov.do/a/d/2533-sector-real"

    # Click :nth-match(:text("2007-2021"), 2)
    with page.expect_download() as download_info:
        page.click('//*[@id="Referencia2007"]/div/table/tbody/tr[2]/td[2]/a')
    download = download_info.value

    # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
    url = page.url
    content = page.locator('//*[@id="Referencia2007"]/div/table/tbody/tr[2]/td[1]').text_content()


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

    with page.expect_download() as download_info:
        page.click('//*[@id="2"]/div/table/tbody/tr[1]/td[2]/a')
    download = download_info.value

    url = page.url
    content = page.locator('//*[@id="2"]/div/table/tbody/tr[1]/td[2]/a').text_content()


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
