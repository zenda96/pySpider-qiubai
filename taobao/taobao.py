#-*- coding:utf-8-*-
# !/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

from pyquery import PyQuery as pq

import re


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=chrome_options)

wait = WebDriverWait(browser, 10)
def search():
    print('正在搜索...')
    browser.get('https://www.taobao.com/')
    try:
        input = wait.until(
            EC.presence_of_element_located((By.ID, "q"))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button"))
        )
        input.send_keys('美食')
        submit.click()
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.total"))            
        )
        get_products()
        return total.text
    except TimeoutException:
        return search()
    finally:
        pass
def next_page(num):
    print('----------------------')
    print('当前页数:'+str(num))
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input"))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit"))
        )
        input.clear()
        input.send_keys(num)
        submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > ul > li.item.active > span"),str(num))            
        )
        get_products()
    except TimeoutException:
       next_page(num)

def get_products():
    wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-itemlist .items .item"))            
    )
    html = browser.page_source
    doc = pq(html)
    items = doc("#mainsrp-itemlist .items .item").items()
    for item in items:
        product={
            'image':item.find('.pic .img').attr("src"),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text()[:-3],
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text(),
        }
        print(product)

def main():
    try:
        total = search()
        total = int(re.search('(\d+)',total).group(1))
        print(total)
        for i in range(2,4):
            next_page(i)
    except Exception:
        print('出错！！')
    finally:
        browser.close()
if __name__=='__main__':
    main()