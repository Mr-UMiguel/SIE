from prefect import task
import datetime
from playwright.sync_api import sync_playwright 


def api(download_path,serieID, start_date):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()

        # Open new page
        page = context.new_page()


        # Go to https://www3.bcb.gov.br/sgspub/consultarvalores/telaCvsSelecionarSeries.paint
        page.goto("https://www3.bcb.gov.br/sgspub/consultarvalores/telaCvsSelecionarSeries.paint")

        # Go to https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries
        page.goto("https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries")


        # Fill input[name="codigo"]
        page.fill("input[name=\"codigo\"]", serieID )

        # Press Enter
        page.press("input[name=\"codigo\"]", "Enter")

        # Check input[name="cbxSelecionaSerie"]
        page.frame(name="iCorpo").check("input[name=\"cbxSelecionaSerie\"]")

        # Click input:has-text("Consultar séries")
        # with page.expect_navigation(url="https://www3.bcb.gov.br/sgspub/consultarvalores/telaCvsSelecionarSeries.paint"):
        with page.expect_navigation():
            page.click("input:has-text(\"Consultar séries\")")


        # Fill input[name="dataInicio"]
        page.fill("input[name=\"dataInicio\"]", start_date)

        # Click text=Visualizar valores
        page.click("text=Visualizar valores")
        # assert page.url == "https://www3.bcb.gov.br/sgspub/consultarvalores/consultarValoresSeries.do?method=consultarValores"

        # Click text=Arquivo CSV
        with page.expect_download() as download_info:
            with page.expect_popup() as popup_info:
                page.click("text=Arquivo CSV")
            page1 = popup_info.value
        download = download_info.value

        # Close page
        page1.close()
        #### PARA GUARDAR EL ARCHIVO ###########
        ### NO MODIFCAR ESTA PARTE 
        download.save_as(download_path+f"/{download.suggested_filename}")
        print(f"""
        **********************************
        File has been successfully downloaded 
        {download_path+f"/{download.suggested_filename}"}
        """)
        # ---------------------
        context.close()
        browser.close()
        return download.suggested_filename

@task(name="BRA-1_01_1",log_stdout=True, max_retries=2,retry_delay=datetime.timedelta(seconds=2))
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



@task(name="BRA-1_11_1",log_stdout=True, max_retries=2,retry_delay=datetime.timedelta(seconds=2))
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

@task(name="BRA-1_17_1",log_stdout=True, max_retries=2,retry_delay=datetime.timedelta(seconds=2))
def e1_17_1(download_path):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://sidra.ibge.gov.br/tabela/1737')

    # Click text=EditorExpandir/reduzir janelaMês [1/507]TudoToggle DropdownTudoMarcadosDesmarcad >> [aria-label="Marcar\ todos\ os\ elementos\ listados"]
        page.click('//*[@id="panel-P-collapse"]/div[2]/div/div[1]/div[1]/div/button[1]')
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
        

