import json
settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']


def run(playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.banguat.gob.gt/

    page.goto("https://www.banguat.gob.gt/es/page/sistema-de-cuentas-nacionales-trimestrales-ano-de-referencia-2013")

    # Click text=Ver formato en Excel período 1T-2013 - 3T-2021
    with page.expect_download() as download_info:
        page.click('//*[@id="content"]/div/article/div/div[1]/table/tbody/tr[2]/td/p[3]/a')
    download = download_info.value
    download.save_as(root_path+f"/EXTRACT-DB/GTM/{download.suggested_filename}")
    # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
    url = page.url
    content = page.locator('//*[@id="content"]/div/article/div/div[1]/table/tbody/tr[2]/td/p[3]/a').text_content()
    # ---------------------

    print(f"""
    **********************************
    {url}
    ----------------------------------
    {content}
    File has been successfully downloaded 
    {root_path+f"/EXTRACT-DB/GTM/{download.suggested_filename}"}
    """)
    
        # ---------------------
    context.close()
    browser.close()


