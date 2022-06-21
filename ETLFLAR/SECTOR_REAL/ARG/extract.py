from playwright.sync_api import sync_playwright 


def _1_01_1(download_path) -> None:
    """
        PIB REAL ARGENTINA
        precios constantes año base 2004
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        # Open new page
        page = context.new_page()

        ######################################################################
        ### ESTO ES LO QUE PROBABLEMENTE DEBE EDITAR EN CASO DE ERROR     ###

        # Go to https://www.indec.gob.ar/
        page.goto("https://www.indec.gob.ar/indec/web/Nivel4-Tema-3-9-47") 


        with page.expect_download() as download_info:
            page.locator('//*[@id="1"]/div[2]/div[1]/div[2]/div/div/a').click()
        download = download_info.value


        #### PARA GUARDAR EL ARCHIVO ###########
        ### NO MODIFCAR ESTA PARTE 
        download.save_as(download_path+f"/{download.suggested_filename}")

        print(f"""
        File has been successfully downloaded as
        ----------------------------------------
            {download_path+f"/{download.suggested_filename}"}
        """)
        # ---------------------
        context.close()
        browser.close()
        
    return download.suggested_filename

def _1_17_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.indec.gob.ar/indec/web/Nivel4-Tema-3-5-31")

        download_locator = '//*[@id="1"]/div[2]/div[1]/div[2]/div/div/a'
        with page.expect_download() as download_info:
            page.locator(download_locator).click()

        download = download_info.value
        
        url = page.url
        content = page.locator(download_locator).text_content()

        ########################################################################
        ### ESTO NO DEBE EDITARLO EN CASO DE ERRO A MENOS QUE SEA NECESARIO ###
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