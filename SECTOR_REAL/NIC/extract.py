from prefect import task
import datetime
import time
from playwright.sync_api import sync_playwright 

@task(name="NIC-1_01_1",log_stdout=True, max_retries=2,retry_delay=datetime.timedelta(seconds=2))
def e1_01_1(playwright, download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(accept_downloads=True)

        # Open new page
        page = context.new_page()

        # Go to https://bcn.gob.ni/cuentas-nacionales-trimestrales
        page.goto("https://bcn.gob.ni/cuentas-nacionales-trimestrales")

        # Click text=Cuentas Nacionales Trimestrales Las Cuentas Nacionales Trimestrales (CNT) confor >> img
        # with page.expect_navigation(url=":"):
        with page.expect_download() as download_info:
            page.click("text=Cuentas Nacionales Trimestrales Las Cuentas Nacionales Trimestrales (CNT) confor >> img")
        download = download_info.value

        url = page.url
        content = page.locator('text=Cuentas Nacionales Trimestrales Las Cuentas Nacionales Trimestrales (CNT) confor >> img').text_content()
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

@task(name="NIC-1_11_1",log_stdout=True, max_retries=2,retry_delay=datetime.timedelta(seconds=2))
def e1_11_1(playwright, download_path) -> None:
    with sync_playwright() as playwright:
        pass


@task(name="NIC-1_17_1",log_stdout=True, max_retries=2,retry_delay=datetime.timedelta(seconds=2))
def e1_17_1(playwright, download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(accept_downloads=True)

        # Open new page
        page = context.new_page()

        # Go to https://bcn.gob.ni/cuentas-nacionales-trimestrales
        page.goto("https://bcn.gob.ni/cuentas-nacionales-trimestrales")

        # Click text=Cuentas Nacionales Trimestrales Las Cuentas Nacionales Trimestrales (CNT) confor >> img
        # with page.expect_navigation(url=":"):
        with page.expect_download() as download_info:
            page.click("text=Cuentas Nacionales Trimestrales Las Cuentas Nacionales Trimestrales (CNT) confor >> img")
        download = download_info.value

        url = page.url
        content = page.locator('text=Cuentas Nacionales Trimestrales Las Cuentas Nacionales Trimestrales (CNT) confor >> img').text_content()
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


