import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']


def run(playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(accept_downloads=True)

    # Open new page
    page = context.new_page()

    # Go to https://bcn.gob.ni/cuentas-nacionales-trimestrales
    page.goto("https://bcn.gob.ni/cuentas-nacionales-trimestrales")

    # Click text=Cuentas Nacionales Trimestrales Las Cuentas Nacionales Trimestrales (CNT) confor >> img
    # with page.expect_navigation(url=":"):
    with page.expect_download() as download_info:
        page.click("text=Cuentas Nacionales Trimestrales Las Cuentas Nacionales Trimestrales (CNT) confor >> img")
    download = download_info.value
    download.save_as(root_path+f"/EXTRACT-DB/NIC/{download.suggested_filename}")

    url = page.url
    content = page.locator('text=Cuentas Nacionales Trimestrales Las Cuentas Nacionales Trimestrales (CNT) confor >> img').text_content()
    # ---------------------

    print(f"""
    **********************************
    {url}
    ----------------------------------
    {content}
    File has been successfully downloaded 
    {root_path+f"/EXTRACT-DB/NIC/{download.suggested_filename}"}
    """)

    # ---------------------
    context.close()
    browser.close()

    # ---------------------
    context.close()
    browser.close()