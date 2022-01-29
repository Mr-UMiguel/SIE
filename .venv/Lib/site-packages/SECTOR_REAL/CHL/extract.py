import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']


def run(playwright, download_path) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://si3.bcentral.cl/Siete
    page.goto("https://si3.bcentral.cl/Siete")

    # Click text=Cuentas Nacionales
    page.click("text=Cuentas Nacionales")
    # assert page.url == "https://si3.bcentral.cl/Siete/ES/Siete/Cuadro/CAP_CCNN/MN_CCNN76/CCNN2013_IMACEC_01"

    # Click text=Producto interno bruto
    page.click("text=Producto interno bruto")

    # Click text=PIB total
    content = page.locator('//*[@id="MN_CCNN76CCNN2013_P0_V2"]').text_content()
    page.click('//*[@id="MN_CCNN76CCNN2013_P0_V2"]')
    # assert page.url == "https://si3.bcentral.cl/Siete/ES/Siete/Cuadro/CAP_CCNN/MN_CCNN76/CCNN2013_P0_V2/CCNN2013_P0_V2"

    # Check .fixed-columns .fixed-table-body #grilla #tbodyGrid tr:nth-child(2) .nw .chkGrid
    page.check(".fixed-columns .fixed-table-body #grilla #tbodyGrid tr:nth-child(2) .nw .chkGrid")

    # Click button:nth-child(6)
    page.click("button:nth-child(6)")

    # # Fill #radioExportV
    # page.fill("#radioExportV", "true")

    # Click #radioExportV
    page.click("#radioExportV")

    # Click #modalExport >> text=Aceptar
    with page.expect_download() as download_info:
        with page.expect_popup() as popup_info:
            page.click("#modalExport >> text=Aceptar")
        page1 = popup_info.value
    download = download_info.value
    # Close page
    page1.close()

    # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
    url = page.url
    
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



