from prefect import task
import datetime
from playwright.sync_api import sync_playwright 

@task(name="BRA-1_01_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_01_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()


        page.goto('https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9300-contas-nacionais-trimestrais.html')

        # Click text=Tabelas
        page.click("text=Tabelas")
        # assert page.url == "https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9300-contas-nacionais-trimestrais.html?=&t=resultados"

        # Click text=Tabelas Completas
        download_locator = 'text=Tabelas Completas'
        with page.expect_download() as download_info:
            page.click(download_locator)
        download = download_info.value

        url = page.url
        content = page.locator(download_locator).text_content()

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



@task(name="BRA-1_11_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_11_1(download_path) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        page.goto("https://www.ibge.gov.br/estatisticas/sociais/trabalho/9171-pesquisa-nacional-por-amostra-de-domicilios-continua-mensal.html?=&t=series-historicas")

        # Select xlsx
        with page.expect_download() as download_info:
            page.select_option("#seriehistorica201755114441729export", "xlsx")
        download = download_info.value

        url = page.url
        content = page.locator('//*[@id="series-historicas"]/h4[1]').text_content()

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

@task(name="BRA-1_17_1",log_stdout=True, max_retries=3,retry_delay=datetime.timedelta(seconds=10))
def e1_17_1(download_path):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://sidra.ibge.gov.br/tabela/1737')

        # Click text=EditorExpandir/reduzir janelaMês [1/506]TudoToggle DropdownTudoMarcadosDesmarcad >> [aria-label="Marcar\ todos\ os\ elementos\ listados"]
        page.click("text=EditorExpandir/reduzir janelaMês [1/506]TudoToggle DropdownTudoMarcadosDesmarcad >> [aria-label=\"Marcar\\ todos\\ os\\ elementos\\ listados\"]")
        # Click text=Download
        page.click("text=Download")
        # Click strong:has-text("Download")
        with page.expect_download() as download_info:
            with page.expect_popup() as popup_info:
                page.click("strong:has-text(\"Download\")")
            page1 = popup_info.value
        download = download_info.value
        # Close page
        page1.close()
        
        url = page.url
        content = 'Tabela 1737 - IPCA - Série histórica com número-índice, variação mensal e variações acumuladas em 3 meses, em 6 meses, no ano e em 12 meses (a partir de dezembro/1979)'

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

