from prefect import task
from prefect.engine.results import LocalResult

import datetime
from playwright.sync_api import sync_playwright 

@task(name="ARG-1_01_1",log_stdout=True, max_retries=2,retry_delay=datetime.timedelta(seconds=2),
      result=LocalResult(location="initial_data.prefect"))
def e1_01_1v(download_path) -> None:
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
        page.goto("https://www.indec.gob.ar") 
        # Click text=ESTADÍSTICAS
        page.click("text=ESTADÍSTICAS")
        # Click text=Cuentas nacionales
        # with page.expect_navigation(url="https://www.indec.gob.ar/indec/web/Nivel3-Tema-3-9"):
        with page.expect_navigation(url="https://www.indec.gob.ar/indec/web/Nivel3-Tema-3-9"):
            page.click("text=Cuentas nacionales")
        # Click text=Agregados macroeconómicos (PIB)
        page.click("text=Agregados macroeconómicos (PIB)")


        # Click #contenidoPrincipal >> :nth-match(div:has-text("PIB Ingreso y ahorro nacional Formación bruta de capital fijo Producto interno b"), 2)
        page.click("#contenidoPrincipal >> :nth-match(div:has-text(\"PIB Ingreso y ahorro nacional Formación bruta de capital fijo Producto interno b\"), 2)")
        

        with page.expect_download() as download_info:
            page.locator('//*[@id="1"]/div[2]/div[1]/div[2]/div/div/a').click()
        download = download_info.value

        url = page.url
        content = page.locator('//*[@id="1"]/div[2]/div[1]/div[2]/div/div/a').text_content()


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

@task(name="ARG-1_11_1",log_stdout=True, max_retries=2,retry_delay=datetime.timedelta(seconds=2))
def e1_11_1v(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        ######################################################################
        ### ESTO ES LO QUE PROBABLEMENTE DEBE EDITAR EN CASO DE ERROR     ###

        # Go to https://www.indec.gob.ar/
        page.goto("https://www.indec.gob.ar/")

        # Click text=ESTADÍSTICAS
        page.click("text=ESTADÍSTICAS")

        # Click text=Trabajo e ingresos
        # with page.expect_navigation(url="https://www.indec.gob.ar/indec/web/Nivel3-Tema-4-31"):
        with page.expect_navigation():
            page.click("text=Trabajo e ingresos")

        # Click text=Mercado de trabajo
        # with page.expect_navigation(url="https://www.indec.gob.ar/indec/web/Nivel4-Tema-4-31-58"):
        with page.expect_navigation():
            page.click("text=Mercado de trabajo")

        # Click text=Mercado de trabajo. Tasas e indicadores socioeconómicos (EPH). Primer trimestre
        # with page.expect_navigation(url=":"):
        with page.expect_download() as download_info:
                page.click('//*[@id="contenidoSecundario"]/div[2]/div[2]/div/div/div/div/a[1]')
        download = download_info.value

        url = page.url
        content = page.locator('//*[@id="contenidoSecundario"]/div[2]/div[2]/div/div/div/div/a[1]').text_content()


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


@task(name="ARG-1_17_1",log_stdout=True, max_retries=2,retry_delay=datetime.timedelta(seconds=2))
def e1_17_1(download_path) -> None:
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


@task(name="ARG-1_22_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_22_1(download_path) -> None:
    pass


