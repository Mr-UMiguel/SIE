from prefect import task
import datetime
import time
from playwright.sync_api import sync_playwright 

@task(name="URY-1_01_1",log_stdout=True, max_retries=2,retry_delay=datetime.timedelta(seconds=2))
def e1_01_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(accept_downloads=True)

        # Open new page
        page = context.new_page()

        # Go to https://bcn.gob.ni/cuentas-nacionales-trimestrales
        page.goto("https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Paginas/Series-Estadisticas-del-PIB-por-industrias.aspx")

        with page.expect_download() as download_info:
            page.locator('//*[@id="ctl00_ctl63_g_00ff9073_4c37_41a1_aebe_602a00cad5ce_ctl00_documents"]/tbody/tr[1]/td[8]/a').click()
        download = download_info.value


        url = page.url
        content = page.locator('//*[@id="ctl00_ctl63_g_00ff9073_4c37_41a1_aebe_602a00cad5ce_ctl00_documents"]/tbody/tr[1]/td[8]/a').text_content()
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

def e1_11_1(playwright,download_path) -> None:
    pass


@task(name="URY-1_17_1",log_stdout=True, max_retries=2,retry_delay=datetime.timedelta(seconds=2))
def e1_17_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(accept_downloads=True)

        # Open new page
        page = context.new_page()

        page.goto("https://www.ine.gub.uy/web/guest/ipc-indice-de-precios-del-consumo")

        page.click('span:has-text(\"Base Diciembre 2010=100\")')
            # Click text=Total País
        page.click("text=Total País")
            # Click text=Índice General y Variación mensual, acumulada del año, últimos doce meses, trime
        with page.expect_download() as download_info:
            page.click('text= Índice General y Variación mensual, acumulada del año, últimos doce meses, trimestre, cuatrimestre y semestre')
        download = download_info.value


        url = page.url
        content = ' Índice General y Variación mensual, acumulada del año, últimos doce meses, trimestre, cuatrimestre y semestre'
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

