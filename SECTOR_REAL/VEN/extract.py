import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']


def run(playwright, download_path) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(accept_downloads=True)

    # Open new page
    page = context.new_page()

    # Go to https://bcn.gob.ni/cuentas-nacionales-trimestrales
    page.goto("http://www.bcv.org.ve/estadisticas/producto-interno-bruto")

    with page.expect_download() as download_info:
        page.locator('//*[@id="block-system-main"]/div/div/div/table/tbody/tr[4]/td[2]/span/a').click()
    download = download_info.value

    url = page.url
    content = page.locator('//*[@id="block-system-main"]/div/div/div/table/tbody/tr[4]/td[2]/span/a').text_content()
    #### PARA GUARDAR EL ARCHIVO ###########
    ### NO MODIFCAR ESTA PARTE 
    download.save_as(download_path+f"/{download.suggested_filename}")

    print(f"""
    **********************************
    {url}
    ----------------------------------
    {content}
    File has been successfully downloaded 
    {download_path+f"/{download.suggested_filename}"}
    """)
    # ---------------------
    context.close()
    browser.close()

    return download.suggested_filename



