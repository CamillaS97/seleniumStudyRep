from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


nav = Firefox() 

nav.get("https://curso-python-selenium.netlify.app/exercicio_02.html")

WebDriverWait(nav, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
p = nav.find_elements_by_tag_name('p')
botao = nav.find_element_by_id('ancora')

while ("ganhou" not in p[-1].text):
    botao.click()
    p = nav.find_elements_by_tag_name('p')


nav.quit()