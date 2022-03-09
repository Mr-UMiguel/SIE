from prefect import task
import datetime
from playwright.sync_api import sync_playwright 

@task(name="DOM-1_01_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_01_1(download_path) -> None:
    with sync_playwright() as playwright:
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

        # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
        url = page.url
        content = page.locator('//*[@id="Referencia2007"]/div/table/tbody/tr[2]/td[1]').text_content()


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
@task(name="DOM-1_11_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_11_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        page.goto('https://www.bancentral.gov.do/a/d/2541-encuesta-continua-encft')

        with page.expect_download() as download_info:
            page.click('//*[@id="2"]/div/table/tbody/tr[1]/td[2]/a')
        download = download_info.value

        url = page.url
        content = page.locator('//*[@id="2"]/div/table/tbody/tr[1]/td[2]/a').text_content()


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



@task(name="DOM-1_17_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_17_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        page.goto('https://www.bancentral.gov.do/a/d/2534-precios')

        download_locator = '//*[@id="IPCBase2020"]/div/table/tbody/tr[1]/td[2]/a'
        with page.expect_download() as download_info:
            page.click(download_locator)
        download = download_info.value

        url = page.url
        content = page.locator('//*[@id="ContentRenderArea"]/div[3]/div/div[1]/h4/a').text_content()


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