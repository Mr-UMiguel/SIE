import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']

series = json.load(open("./series.json","r"))['SECTOR_REAL']['PAN']


def e1_01_1(playwright, download_path) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(accept_downloads=True)

    # Open new page
    page = context.new_page()

    # Go to https://bcn.gob.ni/cuentas-nacionales-trimestrales
    page.goto("https://www.inec.gob.pa/publicaciones/Default2.aspx?ID_CATEGORIA=4&ID_SUBCATEGORIA=26")

    #Click on last update a 
    #Hace falta mejorar debido a que la lista se actualiza 
    page.locator('//*[@id="gvPublicaciones"]/tbody/tr[125]/td[1]/a').click()

    with page.expect_download() as download_info:
        page.locator('//*[@id="gvPublicaciones"]/tbody/tr[3]/td[3]/a[2]').click()
    download = download_info.value


    url = page.url
    content = page.locator('//*[@id="gvPublicaciones"]/tbody/tr[3]/td[3]/a[2]').text_content()
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
    hrefStatic = [ i['hrefStatic'] for i in series if i['flarID']=="1.11.1"]
    page.goto(hrefStatic[0])

    # Click text=Publicaciones
    page.click("text=Publicaciones")
    # assert page.url == "https://www.inec.gob.pa/publicaciones/Default.aspx"
    # Go to https://www.inec.gob.pa/publicaciones/Default2.aspx?ID_CATEGORIA=5&ID_SUBCATEGORIA=38
    page.goto("https://www.inec.gob.pa/publicaciones/Default2.aspx?ID_CATEGORIA=5&ID_SUBCATEGORIA=38")
    # Click text=Estadísticas del Trabajo: Encuesta de Mercado Laboral, Octubre 2021
    page.click("text=Estadísticas del Trabajo: Encuesta de Mercado Laboral, Octubre 2021")


    with page.expect_download() as download_info:
            page.click("text=Cuadro 1APOBLACIÓN DE 15 Y MÁS AÑOS DE EDAD EN LA REPÚBLICA, POR CONDICIÓN EN LA >> :nth-match(a, 3)")
    download = download_info.value
    # Close page


    url = page.url
    content = page.locator('//*[@id="gvPublicaciones"]/tbody/tr[7]/td[2]').text_content()


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



