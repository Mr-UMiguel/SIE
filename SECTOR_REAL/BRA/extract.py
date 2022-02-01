import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']

series = json.load(open("./series.json","r"))['SECTOR_REAL']['BRA']

def e1_01_1(playwright,download_path) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.ibge.gov.br/pt/inicio.html
    hrefStatic = [i['hrefStatic'] for i in series if i['flarID']=="1.01.1"]
    page.goto(hrefStatic[0])

    # Click text=☰
    page.click("text=☰")

    # Click text=Estatísticas
    page.click("text=Estatísticas")

    # Click text=Econômicas
    page.click("text=Econômicas")

    # Click text=Contas nacionais
    # with page.expect_navigation(url="https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais.html"):
    with page.expect_navigation():
        page.click("text=Contas nacionais")

    # Click text=SCNT - Sistema de Contas Nacionais Trimestrais
    # with page.expect_navigation(url="https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9300-contas-nacionais-trimestrais.html"):
    with page.expect_navigation():
        page.click("text=SCNT - Sistema de Contas Nacionais Trimestrais")

    # Go to https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9300-contas-nacionais-trimestrais.html?=&t=o-que-e
    page.goto("https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9300-contas-nacionais-trimestrais.html?=&t=o-que-e")

    # Click text=Tabelas
    page.click("text=Tabelas")
    # assert page.url == "https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9300-contas-nacionais-trimestrais.html?=&t=resultados"

    # Click text=Tabelas Completas
    with page.expect_download() as download_info:
        page.click("text=Tabelas Completas")
    download = download_info.value

    # assert page.url == "https://www.ine.gob.bo/index.php/estadisticas-economicas/pib-y-cuentas-nacionales/producto-interno-bruto-trimestral/producto-interno-bruto-trimestral-intro/#1604584724125-615aec14-e917"
    url = page.url
    content = page.locator('text=Tabelas Completas').text_content()

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


def e1_11_1(playwright,download_path) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.ine.gob.bo/
# Go to https://www.ibge.gov.br/pt/inicio.html
    hrefStatic = [i['hrefStatic'] for i in series if i['flarID']=="1.11.1"]
    page.goto(hrefStatic[0])
    # page.goto("https://www.ibge.gov.br/pt/inicio.html")

    # Click text=☰
    page.click("text=☰")

    # Click text=Estatísticas
    page.click("text=Estatísticas")

    # Click text=Sociais
    page.click("text=Sociais")

    # Click text=Trabalho
    # with page.expect_navigation(url="https://www.ibge.gov.br/estatisticas/sociais/trabalho.html"):
    with page.expect_navigation():
        page.click("text=Trabalho")

    # Click text=PNAD Contínua - Pesquisa Nacional por Amostra de Domicílios Contínua
    # with page.expect_navigation(url="https://www.ibge.gov.br/estatisticas/sociais/trabalho/9171-pesquisa-nacional-por-amostra-de-domicilios-continua-mensal.html"):
    with page.expect_navigation():
        page.click("text=PNAD Contínua - Pesquisa Nacional por Amostra de Domicílios Contínua")

    # Click text=Séries históricas
    # with page.expect_navigation(url="https://www.ibge.gov.br/estatisticas/sociais/trabalho/9171-pesquisa-nacional-por-amostra-de-domicilios-continua-mensal.html?=&t=o-que-e"):
    with page.expect_navigation():
        page.click("text=Séries históricas")

    # Click text=Séries históricas
    page.click("text=Séries históricas")
    # assert page.url == "https://www.ibge.gov.br/estatisticas/sociais/trabalho/9171-pesquisa-nacional-por-amostra-de-domicilios-continua-mensal.html?=&t=series-historicas"

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

