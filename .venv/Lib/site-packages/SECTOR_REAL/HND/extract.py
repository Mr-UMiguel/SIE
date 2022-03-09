from prefect import task
import datetime
from playwright.sync_api import sync_playwright 

@task(name="HND-1_01_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_01_1(download_path) -> None:
    pass


@task(name="HND-1_11_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_11_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        page.goto('https://www.ine.gob.hn/V3/ephpm/')
        # Click text=2021
        page.click("text=2021")
        # Click text=– Mercardo Laboral
        with page.expect_download() as download_info:
            page.click("text=– Mercardo Laboral")

        download = download_info.value
        # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
        url = page.url
        content = page.locator("text=– Mercardo Laboral").text_content()
        
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


@task(name="HND-1_17_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_17_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        page.goto('https://www.bch.hn/estadisticas-y-publicaciones-economicas/publicaciones-de-precios/series-ipc')
        # Click text=2021

        # Click #Encuesta >> text=X
        try:
            page.click("#Encuesta >> text=X")
        except:
            pass

        # Click text=Serie Mensual y Promedio Anual del Índice de Precios al Consumidor (XLS)
        content = page.locator('//*[@id="WebPartWPQ3"]/div[1]/div/div/div[3]/div/div/a[1]/div/span').text_content()
        page.click('//*[@id="WebPartWPQ3"]/div[1]/div/div/div[3]/div/div/a[1]/div/span')
        # assert page.url == "https://www.bch.hn/estadisticos/GIE/_layouts/15/WopiFrame.aspx?sourcedoc=%7B8808A618-19B8-450F-86F4-934B8CD41FEE%7D&file=Serie%20Mensual%20y%20Promedio%20Anual%20del%20%C3%8Dndice%20de%20Precios%20al%20Consumidor.xls&action=default"
        # Click a[role="button"]:has-text("Download")
        with page.expect_download() as download_info:
            page.frame(name="WebApplicationFrame").click("a[role=\"button\"]:has-text(\"Download\")")
        download = download_info.value
        

        download = download_info.value
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
