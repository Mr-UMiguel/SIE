from prefect import task
import datetime
from playwright.sync_api import sync_playwright 

@task(name="ECU-1_01_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_01_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        # Go to https://www.bancentral.gov.do/
        page.goto("https://contenido.bce.fin.ec/home1/estadisticas/cntrimestral/CNTrimestral.jsp")
        # Click text=Boletín de Cuentas Nacionales Trimestrales No. 117, valores constantes USD 2007
        with page.expect_download() as download_info:
            page.frame(name="Data").click("text=Boletín de Cuentas Nacionales Trimestrales No. 117, valores constantes USD 2007 ")
        download = download_info.value

        # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
        url = page.url
        content = 'Boletín de Cuentas Nacionales Trimestrales No. 117, valores constantes USD 2007 '


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

@task(name="ECU-1_11_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_11_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        # Go to https://www.bancentral.gov.do/
        # Go to https://www.ecuadorencifras.gob.ec/trabajo/
        page.goto("https://www.ecuadorencifras.gob.ec/trabajo/")
        # Click img[alt="Elementos\ ENEMDU-02"]
        page.click("img[alt=\"Elementos\\ ENEMDU-02\"]")
        # assert page.url == "https://www.ecuadorencifras.gob.ec/estadisticas-laborales-enero-2022/"
        # Click img[alt="Excel"]
        with page.expect_download() as download_info:
            page.click('//*[@id="content-main"]/div[5]/table[2]/tbody/tr[2]/td[1]/a')
        download = download_info.value

        # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
        url = page.url
        content = page.locator('//*[@id="content"]/div[2]/div/h3').text_content()


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

@task(name="ECU-1_17_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_17_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        page.goto("https://www.ecuadorencifras.gob.ec/indice-de-precios-al-consumidor/")


        page.click('//*[@id="content-full "]/table[1]/tbody/tr/td[1]/a/img')


        with page.expect_download() as download_info:
            page.click('//*[@id="content-main"]/div[3]/table[2]/tbody/tr[2]/td[1]/a/img')
        download = download_info.value

        # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
        url = page.url
        content = page.locator('//*[@id="content"]/div[2]/div/h3').text_content()


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