import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']


series = json.load(open("./series.json","r"))['SECTOR_REAL']['BOL']


def e1_01_1(playwright,download_path) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/
    page.goto("https://www.ine.gob.bo")

    # Click text=Estadísticas económicas
    page.click("text=Estadísticas económicas")
    # page.locator('//*[@id="primary-menu"]/li[3]/a/span/span/center').click()

    # Click text=Cuentas Nacionales
    page.click("text=Cuentas Nacionales")
    # page.locator('//*[@id="primary-menu"]/li[3]/ul/li[1]/a/span/span').click()

    # Click text=Producto Interno Bruto Trimestral
    page.click("text=Producto Interno Bruto Trimestral")
    # page.locator('//*[@id="primary-menu"]/li[3]/ul/li[1]/ul/li[2]/a/span/span').click()
    # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/"
    page.locator('html').click()
    # Click text=Cuadros Estadísticos
    page.click("text=Cuadros Estadísticos")
    # page.locator('//*[@id="content"]/div[1]/div/div/div/div[3]/div/div[1]/ul/li[2]/a/span').click()
    # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"

    # Click text=BOLIVIA: PRODUCTO INTERNO BRUTO A PRECIOS CONSTANTES POR ACTIVIDAD ECONÓMICA SEG
    with page.expect_download() as download_info:
        page.locator('//*[@id="1604584724125-615aec14-e917"]/div[2]/div[2]/ul/li[1]/a').click()
    download = download_info.value

    # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
    url = page.url
    content = page.locator('//*[@id="1604584724125-615aec14-e917"]/div[2]/div[2]/ul/li[1]/a').text_content()
    
    
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



def e1_11_1(playwright,download_path) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.ine.gob.bo/
    hrefStatic = [i['hrefStatic'] for i in series if i['flarID']=="1.11.1"]
    page.goto(hrefStatic[0])

    # Click text=Estadísticas sociales
    page.click("text=Estadísticas sociales")

    # Click a:has-text("Empleo")
    page.click("a:has-text(\"Empleo\")")

    # Click text=Encuesta Continua de Empleo (a partir de 2016)
    page.click("text=Encuesta Continua de Empleo (a partir de 2016)")
    # assert page.url == "https://www.ine.gob.bo/index.php/desocupacion/"

    # # Click text=CUADROS ESTADÍSTICOS POR MES
    page.locator('html').click()
    page.locator('//*[@id="menu-item-43474"]/span/a').click()
    # assert page.url == "https://www.ine.gob.bo/index.php/desocupacion/#"

    # Click #menu-item-43646 >> text=INDICADORES DE EMPLEO
    page.click("#menu-item-43646 >> text=INDICADORES DE EMPLEO")
    # assert page.url == "https://www.ine.gob.bo/index.php/desocupacion/#"

    # Click text=Bolivia: Principales indicadores de empleo por mes, según grupo de departamentos
    page.click("text=Bolivia: Principales indicadores de empleo por mes, según grupo de departamentos")
    # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-sociales/bolivia-principales-indicadores-de-empleo-por-mes-segun-grupo-de-departamentos/"

    # Click a:has-text("Bolivia: Principales indicadores de empleo por mes, según grupo de departamentos")
    with page.expect_download() as download_info:
        page.click('//*[@id="content"]/div/div/div/div/div/div/ul/li/a')
    download = download_info.value
    # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-sociales/bolivia-principales-indicadores-de-empleo-por-mes-segun-grupo-de-departamentos/"

    # ---------------------
    # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
    url = page.url
    content = page.locator('//*[@id="content"]/div/div/div/div/div/div/ul/li/a').text_content()
    
    
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

