import json


settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']


def run(playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(accept_downloads=True)

    # Open new page
    page = context.new_page()
    
    #go to
    page.goto('https://www.inei.gob.pe/estadisticas/indice-tematico/economia')

    with page.expect_downloads as download_info:
        page.locator('//*[@id="contenido"]/ul/li[2]/ul/li/ul/li[1]/ul/li[1]/a').click()
    download = download_info.value
    download.save_as(root_path+f"/EXTRACT-DB/PER/{download.suggested_filename}")


    url = page.url
    content = page.locator('//*[@id="contenido"]/ul/li[2]/ul/li/ul/li[1]/ul/li[1]/a').text_content()
    # ---------------------

    print(f"""
    **********************************
    {url}
    ----------------------------------
    {content}
    File has been successfully downloaded 
    {root_path+f"/EXTRACT-DB/PER/{download.suggested_filename}"}
    """)

    # ---------------------
    context.close()
    browser.close()