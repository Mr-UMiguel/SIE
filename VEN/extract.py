import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']


def run(playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(accept_downloads=True)

    # Open new page
    page = context.new_page()

    # Go to https://bcn.gob.ni/cuentas-nacionales-trimestrales
    page.goto("http://www.bcv.org.ve/estadisticas/producto-interno-bruto")

    with page.expect_download() as download_info:
        page.locator('//*[@id="block-system-main"]/div/div/div/table/tbody/tr[4]/td[2]/span/a').click()
    download = download_info.value
    download.save_as(root_path+f"/EXTRACT-DB/VEN/{download.suggested_filename}")


    url = page.url
    content = page.locator('//*[@id="block-system-main"]/div/div/div/table/tbody/tr[4]/td[2]/span/a').text_content()
    # ---------------------

    print(f"""
    **********************************
    {url}
    ----------------------------------
    {content}
    File has been successfully downloaded 
    {root_path+f"/EXTRACT-DB/VEN/{download.suggested_filename}"}
    """)

    # ---------------------
    context.close()
    browser.close()




