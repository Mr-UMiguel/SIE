import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']


def run(playwright) -> None:
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
    download.save_as(root_path+f"/EXTRACT-DB/BOL/{download.suggested_filename}")

    # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
    url = page.url
    content = page.locator('//*[@id="1604584724125-615aec14-e917"]/div[2]/div[2]/ul/li[1]/a').text_content()
    # ---------------------

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