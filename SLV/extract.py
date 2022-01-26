import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']


def run(playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(accept_downloads=True)

    # Open new page
    page = context.new_page()

    # Go to https://bcn.gob.ni/cuentas-nacionales-trimestrales
    page.goto("https://www.bcr.gob.sv/bcrsite/?cat=1000&lang=es")

    # Locator
    page.locator('//*[@id="esq_43"]/div[2]/div[1]/a').click()

    # Locator
    page.locator('//*[@id="bcr_cuerpo"]/div[2]/form/div[4]/div[2]/div[4]/div[1]/div[1]/div/a').click()

    with page.expect_download() as download_info:
        page.locator('//*[@id="bcr_cuerpo"]/div[2]/form/div[5]/div[1]/div[2]/a').click()
    download = download_info.value
    download.save_as(root_path+f"/EXTRACT-DB/SLV/{download.suggested_filename}")


    url = page.url
    content = page.locator('//*[@id="bcr_cuerpo"]/div[2]/form/div[4]/div[2]/div[4]/div[1]/div[1]/div/a').text_content()
    # ---------------------

    print(f"""
    **********************************
    {url}
    ----------------------------------
    {content}
    File has been successfully downloaded 
    {root_path+f"/EXTRACT-DB/SLV/{download.suggested_filename}"}
    """)

    # ---------------------
    context.close()
    browser.close()


