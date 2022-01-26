import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']


def run(playwright) -> None:
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
    download.save_as(root_path+f"/EXTRACT-DB/PAN/{download.suggested_filename}")


    url = page.url
    content = page.locator('//*[@id="gvPublicaciones"]/tbody/tr[3]/td[3]/a[2]').text_content()
    # ---------------------

    print(f"""
    **********************************
    {url}
    ----------------------------------
    {content}
    File has been successfully downloaded 
    {root_path+f"/EXTRACT-DB/PAN/{download.suggested_filename}"}
    """)

    # ---------------------
    context.close()
    browser.close()
    