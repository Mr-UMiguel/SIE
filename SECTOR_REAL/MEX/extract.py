from prefect import task
import datetime
import time
from playwright.sync_api import sync_playwright 

@task(name="MEX-1_01_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_01_1(download_path) -> None:
    with sync_playwright() as playwright:        
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(accept_downloads=True)

        # Open new page
        page = context.new_page()

        # Go to https://www.inegi.org.mx/temas/pib/
        page.goto("https://www.inegi.org.mx/temas/pib/")

        # 0× click
        page.click("html")
        # assert page.url == "https://www.inegi.org.mx/temas/pib/#Herramientas"

        # Click text=Tabulados
        page.click("text=Tabulados")
        # assert page.url == "https://www.inegi.org.mx/temas/pib/#Tabulados"

        # Click text=Series originales
        page.click("text=Series originales")

        # Click text=Serie detallada
        page.click("text=Serie detallada")

        # Click text=Valores constantes a precios de 2013
        page.click("text=Valores constantes a precios de 2013")

        # Click [aria-label="Descarga\ el\ archivo\ Millones\ de\ pesos\ a\ precios\ de\ 2013\ en\ formato\ xlsx"] img
        # with page.expect_navigation(url=":"):

        with page.expect_download() as download_info:
            page.click('//*[@id="tblDescargaArchivos_descargaMasiva"]/tbody/tr[7]/td[3]/div/a')
        download = download_info.value

        # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
        url = page.url
        content = page.locator('//*[@id="tblDescargaArchivos_descargaMasiva"]/tbody/tr[7]/td[3]/div/a').text_content()
        
        
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
@task(name="MEX-1_11_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_11_1(download_path) -> None:
    with sync_playwright() as playwright:        
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()


        page.goto('https://www.inegi.org.mx/temas/empleo/')

        # Click #btn_tablagraf_gral0
        page.click("#btn_tablagraf_gral0")
        # Click #btn_exportaCSVgraf_gral0
        with page.expect_download() as download_info:
            page.click("#btn_exportaCSVgraf_gral0")
        download = download_info.value


        url = page.url
        content = page.locator('#btn_exportaCSVgraf_gral0').text_content()


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


@task(name="MEX-1_17_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_17_1(download_path):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(ignore_https_errors=True, accept_downloads=True)

        # Open new page
        page = context.new_page()

        page.goto('https://www.inegi.org.mx/app/indicesdeprecios/Estructura.aspx?idEstructura=112001300020&T=%C3%8Dndices%20de%20Precios%20al%20Consumidor&ST=Principales%20%C3%ADndices%20(mensual)')
        # Click #btn_tablagraf_gral0
        page.click('//*[@id="PrincipalContainer"]/div/div/div[1]/img[2]')
        # Click #btn_exportaCSVgraf_gral0

        content = page.locator('//*[@id="Titulo1_Estructura"]/h4').text_content()
        page.select_option('//*[@id="MainContent_wuc_BarraHerramientas1_ddlAnioI"]','1969')

        with page.expect_download() as download_info:
            page.selector("text=Exportar").click()
        download = download_info.value


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