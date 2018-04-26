#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from requests.exceptions import RequestException
import re 
import json
from multiprocessing import Pool


def get_one_page(url):
    '''
        获取一页的列表
    '''
    headers={
        'Referer':'http://maoyan.com/board',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    try:
        response = requests.get(url,headers=headers)
        if(response.status_code==200):
            return response.text
        else:
            return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<div class="movie-item-info">.*?<a.*?title="(.*?)" data-act="boarditem-click".*?</a>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>.*?<i class="integer">(\d+)\.</i>.*?<i class="fraction">(\d+)</i>',re.S)
    res = re.findall(pattern,html)
    for item in res:
        yield{
            'name':item[0].strip(),
            'star':item[1].strip()[3:],
            'time':item[2].strip()[5:],
            'score':item[3]+'.'+item[4]
        }git 

def write_to_txt(txt):
    with open('top100.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(txt,ensure_ascii=False)+'\n')
        f.close()

def main(offset):
    url ="http://maoyan.com/board/4?offset="
    html =get_one_page(url+str(offset))
    for item in parse_one_page(html):
        write_to_txt(item)
        print(item)

if __name__ == '__main__':
    for i in range(10):
        main(i*10)

