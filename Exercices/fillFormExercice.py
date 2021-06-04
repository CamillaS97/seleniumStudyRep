from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse


def fillForm(browser, nome, email, senha, telefone):
    browser.find_element_by_id('nome').send_keys(nome)
    browser.find_element_by_id('email').send_keys(email)
    browser.find_element_by_id('senha').send_keys(senha)
    browser.find_element_by_id('telefone').send_keys(telefone)
    browser.find_element_by_id('btn').click()


luffy = Firefox()
luffy.get('https://selenium.dunossauro.live/exercicio_04.html')

WebDriverWait(luffy, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "form")))

structure = {
    'nome': 'Cabilla',
    'email': 'cabillasilvestre@rawtmail.com',
    'senha': 'senha123',
    'telefone': '81982606693'
}

fillForm(luffy, **structure)

WebDriverWait(luffy, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "textarea")))

parsed_url = urlparse(luffy.current_url)
result = luffy.find_element_by_tag_name('textarea').text
print(result)
query = parsed_url.query
query = query.replace('&btn=Enviar%21', '')
query = query.replace('%40', '@')
query = '{\'' + query + '\'}'
query = query.replace('=', '\': \'')
final_query = query.replace('&', '\', \'')

assert(final_query == result)

luffy.quit()
