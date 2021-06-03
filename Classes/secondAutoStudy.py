from selenium.webdriver import Firefox
from urllib.parse import urlparse

browser = Firefox()
browser.get("http://selenium.dunossauro.live/aula_04_b.html")

btn_one = browser.find_element_by_id("box-1")
btn_two = browser.find_element_by_id("box-2")
btn_three = browser.find_element_by_id("box-3")
btn_four = browser.find_element_by_id("box-4")

btn_four.click()
btn_one.click()
btn_three.click()
btn_two.click()
unparsed_url = browser.current_url
parsed_url = urlparse(unparsed_url)

print(unparsed_url)
print(parsed_url)

testNumber = 2
