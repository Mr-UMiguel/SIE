import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']


def run(playwright) -> None:
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
    download.save_as(root_path+f"/EXTRACT-DB/MEX/{download.suggested_filename}")

    # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
    url = page.url
    content = page.locator('//*[@id="tblDescargaArchivos_descargaMasiva"]/tbody/tr[7]/td[3]/div/a').text_content()
    # ---------------------

    print(f"""
    **********************************
    {url}
    ----------------------------------
    {content}
    File has been successfully downloaded 
    {root_path+f"/EXTRACT-DB/MEX/{download.suggested_filename}"}
    """)

    # ---------------------
    context.close()
    browser.close()

