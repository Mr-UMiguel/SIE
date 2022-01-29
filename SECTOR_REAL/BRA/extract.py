import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']

def e1_01_1(playwright,download_path) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.ibge.gov.br/pt/inicio.html
    page.goto("https://www.ibge.gov.br/pt/inicio.html")

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