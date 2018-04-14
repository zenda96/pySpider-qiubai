from selenium import webdriver
import requests

browser = webdriver.Chrome()
# html = requests.get('https://www.taobao.com')
# print(html)
try:
    browser.get('https://www.taobao.com')
    print(browser.page_source)
finally:
    browser.close()
    print()