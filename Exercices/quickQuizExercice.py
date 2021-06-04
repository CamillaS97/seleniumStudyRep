from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse

browser = Firefox()

browser.get('https://selenium.dunossauro.live/exercicio_03.html')

WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "h1")))

start = browser.find_element_by_partial_link_text("por aqui")
start.click()

WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "h1")))

answer = browser.find_element_by_xpath("//a[@attr='errado']")
answer.click()

WebDriverWait(browser, 30).until(
    EC.presence_of_element_located((By.TAG_NAME, "h1")))

answer = browser.find_element_by_link_text(browser.title)
answer.click()

WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "h1")))

parsed_url = urlparse(browser.current_url)
url_path = parsed_url.path
url_path = url_path.replace('/', '')
# url_path = url_path.replace('p', 'b') # Forcing wrong answer

answer = browser.find_element_by_link_text(url_path)
answer.click()

WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "pre")))

try:
    result = browser.find_element_by_tag_name('p')
    message = result.text
except Exception:
    message = "error"


if "refresh" in message:
    browser.refresh()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "pre")))

    result = browser.find_element_by_tag_name('pre')
    print(result.text)
    browser.quit()

else:
    result = browser.find_element_by_tag_name('pre')
    print(result.text)
    browser.quit()
