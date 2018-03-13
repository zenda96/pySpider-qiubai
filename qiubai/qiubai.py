#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re

def getMore(num):
    '''
        如果有查看全文的话 进入另外一个页面爬取全文
    '''
    get = requests.get('https://www.qiushibaike.com/article/'+num).text
    moreContent = BeautifulSoup(get,"html.parser")
    moreText = moreContent.find(id="single-next-link").find("div",class_="content").get_text()
    return moreText

def getJoke(num):
    '''
        获取每个笑话并写入txt
    '''
    url = "https://www.qiushibaike.com/8hr/page/" + str(num)
    html = requests.get(url).text
    bsObj = BeautifulSoup(html,"html.parser")
    articles = bsObj.find_all('a',href=re.compile('^\/article\/(\d)+'),class_="contentHerf")
    with open('糗百笑话.txt','a',encoding='gbk', errors='ignore') as f:
        for index ,article in enumerate(articles):
            f.write('_________________________________第'+str(index) + '个笑话______________________________')
            more = False 
            if article.find(class_="content").find('span',class_="contentForAll"):
                numObj = re.search('^/article/(\d+)',article['href'])
                if numObj:
                    num = numObj.group(1)
                    f.write(getMore(num))
            else:
                f.write(article.find(class_="content").find('span',class_=False).get_text())
    print('ok')

def getPage(num):
    '''
        爬取第二页第三页。。。。
    '''
    while num:
        print("*********第 %d 页" %num);
        getJoke(num)
        num -=1
    
if __name__=="__main__":
    getPage(10)
