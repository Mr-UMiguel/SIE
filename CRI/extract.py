import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']

def run(playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.bccr.fi.cr/SitePages/Inicio.aspx
    page.goto("https://gee.bccr.fi.cr/indicadoreseconomicos/Cuadros/frmVerCatCuadro.aspx?idioma=1&CodCuadro=%205803")

    with page.expect_download() as download_info:
        page.click('//*[@id="Form1"]/table[3]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[15]/img')
    download = download_info.value
    download.save_as(root_path+f"/EXTRACT-DB/CRI/{download.suggested_filename}")

    # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
    url = page.url
    content = page.locator('//*[@id="Table0"]/tbody/tr[2]/td/span').text_content()
    # ---------------------

    print(f"""
    **********************************
    {url}
    ----------------------------------
    {content}
    File has been successfully downloaded 
    {root_path+f"/EXTRACT-DB/CRI/{download.suggested_filename}"}
    """)

    # ---------------------
    context.close()
    browser.close()




