from prefect import task
import datetime
import time
from playwright.sync_api import sync_playwright 

@task(name="SLV-1_01_1",log_stdout=True, max_retries=2,retry_delay=datetime.timedelta(seconds=2))
def e1_01_1(download_path) -> None:
    with sync_playwright() as playwright:
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


        url = page.url
        content = page.locator('//*[@id="bcr_cuerpo"]/div[2]/form/div[4]/div[2]/div[4]/div[1]/div[1]/div/a').text_content()
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

@task(name="SLV-1_11_1",log_stdout=True, max_retries=2,retry_delay=datetime.timedelta(seconds=2))
def e1_11_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        page.goto('http://aplicaciones.digestyc.gob.sv/estadisticas.empleo/estadisticas_empleo/index.aspx')

        page.click("//html/body/div[2]/div[1]/div[1]/div[15]/img")


        with page.expect_download() as download_info:
            page.click('//*[@id="arbol_archivos"]/ul/li[8]/a')
        download = download_info.value

        url = page.url
        content = page.locator('//*[@id="arbol_archivos"]/ul/li[8]/a').text_content()


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

@task(name="SLV-1_17_1",log_stdout=True, max_retries=2,retry_delay=datetime.timedelta(seconds=2))
def e1_17_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        page.goto('https://www.bcr.gob.sv/bcrsite/?cdr=123&lang=es')

        page.click('//*[@id="bcr_cuerpo"]/div[2]/form/div[4]/div[2]/div[4]/div[1]/div[1]/div/a')


        with page.expect_download() as download_info:
            page.click('//*[@id="bcr_cuerpo"]/div[2]/form/div[5]/div[1]/div[2]/a')
        download = download_info.value

        url = page.url
        content = 'IV.19  Índice de Precios al consumidor  (IPC) Base dic. 2009  e Inflación'


        #### PARA GUARDAR EL ARCHIVO ###########
        ### NO MODIFCAR ESTA PARTE 
        download.save_as(f"{download_path}/1_17_1.xls")

        print(f"""
        **********************************
        {url}
        ----------------------------------
        {content}
        File has been successfully downloaded 
        {download_path+f"/1_17_1.xls"}
        """)
        # ---------------------
        context.close()
        browser.close()

        return "1_17_1.xls"

