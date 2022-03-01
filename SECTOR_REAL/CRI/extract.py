from prefect import task
import datetime
from playwright.sync_api import sync_playwright 

@task(name="CRI-1_01_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_01_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        # Go to https://www.bccr.fi.cr/SitePages/Inicio.aspx
        page.goto("https://gee.bccr.fi.cr/indicadoreseconomicos/Cuadros/frmVerCatCuadro.aspx?idioma=1&CodCuadro=%205803")

        with page.expect_download() as download_info:
            page.click('//*[@id="Form1"]/table[3]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[15]/img')
        download = download_info.value

        # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
        url = page.url
        content = page.locator('//*[@id="Table0"]/tbody/tr[2]/td/span').text_content()


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
@task(name="CRI-1_11_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_11_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        page.goto('https://gee.bccr.fi.cr/indicadoreseconomicos/Cuadros/frmVerCatCuadro.aspx?idioma=1&CodCuadro=%205504')

        with page.expect_download() as download_info:
            page.click('//*[@id="Form1"]/table[3]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[15]/img')
        download = download_info.value

        url = page.url
        content = page.locator('//*[@id="Table0"]/tbody/tr[2]/td/span').text_content()


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


# 1.17.1 CPI
@task(name="CRI-1_17_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_17_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        page.goto('https://gee.bccr.fi.cr/indicadoreseconomicos/Cuadros/frmVerCatCuadro.aspx?idioma=1&CodCuadro=%202732')

        with page.expect_download() as download_info:
            page.click('//*[@id="Form1"]/table[3]/tbody/tr[5]/td/table/tbody/tr[2]/td/table/tbody/tr/td[15]/img')
        download = download_info.value

        url = page.url
        content = page.locator('//*[@id="Table0"]/tbody/tr[2]/td/span').text_content()


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