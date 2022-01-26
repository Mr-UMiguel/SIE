import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']


def run(playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads= True )

    # Open new page
    page = context.new_page()

    # Go to https://www.dane.gov.co/index.php
    page.goto("https://www.dane.gov.co/index.php")

    # Click text=Estadísticas por tema Economía Comercio internacional Comercio interno Construcc >> em
    page.click("text=Estadísticas por tema Economía Comercio internacional Comercio interno Construcc >> em")

    # Click text=Cuentas nacionales
    page.click("text=Cuentas nacionales")
    # assert page.url == "https://www.dane.gov.co/index.php/estadisticas-por-tema/cuentas-nacionales"

    # Click text=PIB nacional trimestral (coyuntural) Indicador de Seguimiento a la Economía -ISE >> a
    page.click("text=PIB nacional trimestral (coyuntural) Indicador de Seguimiento a la Economía -ISE >> a")
    # assert page.url == "https://www.dane.gov.co/index.php/estadisticas-por-tema/cuentas-nacionales/cuentas-nacionales-trimestrales"

    # Click text=Información histórica
    page.click("text=Información histórica")
    # assert page.url == "https://www.dane.gov.co/index.php/estadisticas-por-tema/cuentas-nacionales/cuentas-nacionales-trimestrales/historicos-producto-interno-bruto-pib"

    # Click text=PIB a precios constantes
    with page.expect_download() as download_info:
        page.click('//*[@id="base-2015"]/table[1]/tbody/tr[2]/td[3]/ul/li[1]/a')
    download = download_info.value
    download.save_as(root_path+f"/EXTRACT-DB/COL/{download.suggested_filename}")

    # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
    url = page.url
    content = page.locator('//*[@id="base-2015"]/table[1]/tbody/tr[2]/td[3]/ul/li[1]/a').text_content()
    # ---------------------

    print(f"""
    **********************************
    {url}
    ----------------------------------
    {content}
    File has been successfully downloaded 
    {root_path+f"/EXTRACT-DB/COL/{download.suggested_filename}"}
    """)

    # ---------------------
    context.close()
    browser.close()

