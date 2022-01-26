import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']


def run(playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(accept_downloads=True)

    # Open new page
    page = context.new_page()

    # Go to https://bcn.gob.ni/cuentas-nacionales-trimestrales
    page.goto("https://www.bcp.gov.py/anexo-estadistico-del-informe-economico-i365")

    with page.expect_download() as download_info:
        page.locator('//*[@id="content-interna"]/div[2]/div[2]/div/p[2]/a').click()
    download = download_info.value
    download.save_as(root_path+f"/EXTRACT-DB/PRY/{download.suggested_filename}")


    url = page.url
    content = page.locator('//*[@id="content-interna"]/div[2]/div[2]/div/p[2]/a').text_content()
    # ---------------------

    print(f"""
    **********************************
    {url}
    ----------------------------------
    {content}
    File has been successfully downloaded 
    {root_path+f"/EXTRACT-DB/PRY/{download.suggested_filename}"}
    """)

    # ---------------------
    context.close()
    browser.close()