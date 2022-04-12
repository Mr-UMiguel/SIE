from prefect import task
import datetime
import time
from playwright.sync_api import sync_playwright 

@task(name="PRY-base",log_stdout=True, max_retries=2,retry_delay=datetime.timedelta(seconds=2))
def base(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(accept_downloads=True)

        # Open new page
        page = context.new_page()

        # Go to https://bcn.gob.ni/cuentas-nacionales-trimestrales
        page.goto("https://www.bcp.gov.py/anexo-estadistico-del-informe-economico-i365")

        with page.expect_download() as download_info:
            page.locator('//*[@id="content-interna"]/div[2]/div[2]/div/p[2]/a').click()
        download = download_info.value


        url = page.url
        content = page.locator('//*[@id="content-interna"]/div[2]/div[2]/div/p[2]/a').text_content()

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

@task(name="PRY-1_11_1",log_stdout=True, max_retries=2,retry_delay=datetime.timedelta(seconds=2))
def e1_11_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()


        page.goto('https://www.ine.gov.py/default.php?publicacion=3')
        # # Click text=ESTADÍSTICA POR TEMA
        # page.click("text=ESTADÍSTICA POR TEMA")
        # # Click text=Empleo
        # page.click("text=Empleo")
        # # assert page.url == "https://www.ine.gov.py/default.php?publicacion=3"
        # # Click text=Publicaciones
        page.click("text=Publicaciones")
        # Click text=Ver documento
        page.click("text=Ver documento")
        # assert page.url == "https://www.ine.gov.py/publication-single.php?codec=MTc0"
        # Click text=Cuadros
        with page.expect_download() as download_info:
            page.click("text=Cuadros")
        download = download_info.value

        url = page.url
        content = page.locator('//html/body/div[1]/div/div/header/h1').text_content()


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
