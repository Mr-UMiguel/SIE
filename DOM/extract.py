import json
settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']

def run(playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.bancentral.gov.do/
    page.goto("https://www.bancentral.gov.do/")

    # Click text=Estadísticas
    page.click("text=Estadísticas")

    # Click text=Sector Real
    page.click("text=Sector Real")
    # assert page.url == "https://www.bancentral.gov.do/a/d/2533-sector-real"

    # Click :nth-match(:text("2007-2021"), 2)
    with page.expect_download() as download_info:
        page.click('//*[@id="Referencia2007"]/div/table/tbody/tr[2]/td[2]/a')
    download = download_info.value
    download.save_as(root_path+f"/EXTRACT-DB/DOM/{download.suggested_filename}")

    # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
    url = page.url
    content = page.locator('//*[@id="Referencia2007"]/div/table/tbody/tr[2]/td[1]').text_content()
    # ---------------------

    print(f"""
    **********************************
    {url}
    ----------------------------------
    {content}
    File has been successfully downloaded 
    {root_path+f"/EXTRACT-DB/DOM/{download.suggested_filename}"}
    """)

    # ---------------------
    context.close()
    browser.close()