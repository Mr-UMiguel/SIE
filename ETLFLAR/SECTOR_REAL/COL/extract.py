from prefect import task
import datetime
from playwright.sync_api import sync_playwright 

@task(name="COL-1_01_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_01_1v(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads= True )

        # Open new page
        page = context.new_page()

        # Go to https://www.dane.gov.co/index.php
        page.goto('https://www.dane.gov.co/index.php/estadisticas-por-tema/cuentas-nacionales/cuentas-nacionales-trimestrales/pib-informacion-tecnica')
        # Click text=PIB a precios constantes
        download_locator = '//*[@id="economia"]/section/div[2]/div[3]/table/tbody[2]/tr[1]/td[5]/a'
        with page.expect_download() as download_info:
            page.click(download_locator)
        download = download_info.value

        # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
        url = page.url
        content = page.locator(download_locator).text_content()
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



# 1.11.1 Desempleo

@task(name="COL-1_11_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_11_1v(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads= True )

        # Open new page
        page = context.new_page()

        # Go to https://www.dane.gov.co/index.php
        page.goto('https://www.dane.gov.co/index.php/estadisticas-por-tema/mercado-laboral/empleo-y-desempleo')
        # Click text=PIB a precios constantes
        download_locator = '//*[@id="empleo-y-desempleo"]/div/div[2]/div[2]/table/tbody/tr[4]/td[5]/a'
        with page.expect_download() as download_info:
            page.click(download_locator)
        download = download_info.value

        url = page.url
        content = page.locator(download_locator).text_content()
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

# 1.17.1 IPC
@task(name="COL-1_17_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_17_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads=True )

        # Open new page
        page = context.new_page()

        # Go to https://www.dane.gov.co/index.php
        page.goto('https://www.banrep.gov.co/es/estadisticas/catalogo')

        # Click text=Serie inflación total y meta / Información disponible desde enero 1993 >> img
        with page.expect_popup() as popup_info:
            page.click('text=Serie inflación total y meta / Información disponible desde enero 1993 >> img')
            page1 = popup_info.value
            with page1.expect_download() as download_info: 
                download = download_info.value
        page1.close()
        # Close page
        


        url = page.url
        content = page.locator('text=Serie inflación total y meta / Información disponible desde enero 1993 >> img').text_content()
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




