import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']


def run(playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(accept_downloads=True)

    # Open new page
    page = context.new_page()

    # Go to https://bcn.gob.ni/cuentas-nacionales-trimestrales
    page.goto("https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Paginas/Series-Estadisticas-del-PIB-por-industrias.aspx")

    with page.expect_download() as download_info:
        page.locator('//*[@id="ctl00_ctl63_g_00ff9073_4c37_41a1_aebe_602a00cad5ce_ctl00_documents"]/tbody/tr[1]/td[8]/a').click()
    download = download_info.value
    download.save_as(root_path+f"/EXTRACT-DB/URY/{download.suggested_filename}")


    url = page.url
    content = page.locator('//*[@id="ctl00_ctl63_g_00ff9073_4c37_41a1_aebe_602a00cad5ce_ctl00_documents"]/tbody/tr[1]/td[8]/a').text_content()
    # ---------------------

    print(f"""
    **********************************
    {url}
    ----------------------------------
    {content}
    File has been successfully downloaded 
    {root_path+f"/EXTRACT-DB/URY/{download.suggested_filename}"}
    """)

    # ---------------------
    context.close()
    browser.close()
    