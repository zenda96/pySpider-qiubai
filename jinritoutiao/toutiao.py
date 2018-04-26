#--*-- coding:utf-8 --*--
# !/usr/bim/env python3

import requests
import re 
from  bs4  import BeautifulSoup 
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
import pymongo
import os
from hashlib import md5

from sqlconfig import *

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

headers = {
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9',
'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

def get_page_index(offset,keyword):
    data = {
        'offset':offset,
        'format':'json',
        'keyword':keyword,
        'autoload':'true',
        'count':20,
        'cur_tab':1,
        'from':'gallery',
    }
    url='https://www.toutiao.com/search_content/?'+urlencode(data)
    reponse = requests.get(url)
    try:
        if reponse.status_code==200:
            return reponse.text
        else:
            return None
    except RequestException:
        print('请求索引页出错')
        return None

def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    reponse = requests.get(url,headers=headers)
    try:
        if reponse.status_code==200:
            return reponse.text
        else:
            return None
    except RequestException:
        print('请求图片出错',url)
        return None

def parse_page_detail(html,url):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    image_pattern = re.compile('gallery: JSON.parse\("(.*?)"\),.*?siblingList:',re.S)
    image_result = re.search(image_pattern,html)
    if image_result:
        tempt = image_result.group(1)
        tempt = tempt.replace(r'\"','"')
        tempt = tempt.replace(r'\\','\\')
        data = json.loads(tempt)
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images:download_image(image)
            return{
                'title':title,
                'images':images,
                'url':url
            }
    else:
        print('未匹配到结果')   

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('插入成功')
        return True
    return False

def download_image(url):
    print('----------正在下载'+url)
    reponse = requests.get(url,headers=headers)
    try:
        if reponse.status_code==200:
            save_image(reponse.content)
        else:
            return None
    except RequestException:
        print('请求详情页出错',url)
        return None

def save_image(content):
    file_path = '{0}/toutiaoimages/{1}.{2}'.format(os.getcwd(),md5(content).hexdigest(),'jpg')
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)

def main():
    html = get_page_index(0,'街拍')
    for url in parse_page_index(html):
        if url:
            url =  re.sub('(group/(\d+))',r'a\2',url)
            detail_html = get_page_detail(url)
            result = parse_page_detail(detail_html,url)
            # save_to_mongo(result)
            print(result)
    
if __name__ =='__main__':
    main()
