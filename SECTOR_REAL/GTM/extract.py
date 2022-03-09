from prefect import task
import datetime
from playwright.sync_api import sync_playwright 

@task(name="GTM-1_01_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_01_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        # Go to https://www.banguat.gob.gt/

        page.goto("https://www.banguat.gob.gt/es/page/sistema-de-cuentas-nacionales-trimestrales-ano-de-referencia-2013")

        # Click text=Ver formato en Excel período 1T-2013 - 3T-2021
        with page.expect_download() as download_info:
            page.click('//*[@id="content"]/div/article/div/div[1]/table/tbody/tr[2]/td/p[3]/a')
        download = download_info.value
        # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
        url = page.url
        content = page.locator('//*[@id="content"]/div/article/div/div[1]/table/tbody/tr[2]/td/p[3]/a').text_content()
        
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

def e1_11_1() -> None:
    pass




@task(name="GTM-1_17_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_17_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        # Go to https://www.banguat.gob.gt/
        page.goto('http://www.banguat.gob.gt/inc/ver.asp?id=/estaeco/sr/sr005')

        download_locator = '//*[@id="tit"]/table/tbody/tr[1]/td/table/tbody/tr/td[3]/a'
        with page.expect_download() as download_info:
            page.click(download_locator)

        download = download_info.value

        # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
        url = page.url
        content = page.locator('//*[@id="sr002_106"]/table/tbody/tr[1]/td[3]/a').text_content()
        
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