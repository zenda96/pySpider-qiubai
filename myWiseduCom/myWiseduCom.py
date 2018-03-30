#-*- coding:utf-8 -*-
#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

session = requests.Session()
url = 'http://cas.wisedu.com/authserver/login?service=http%3A%2F%2Fmy.wisedu.com%2Flogin%3Fservice%3Dhttp%3A%2F%2Fmy.wisedu.com%2Fnew%2Findex.html'

rep = session.get(url)
html = rep.text
# print(html)
bshtml = BeautifulSoup(html,'html.parser')
lt = bshtml.find("input",attrs={"type":"hidden","name":"lt"})["value"]
dllt = bshtml.find("input",attrs={"type":"hidden","name":"dllt"})["value"]
execution = bshtml.find("input",attrs={"type":"hidden","name":"execution"})["value"]
_eventId = bshtml.find("input",attrs={"type":"hidden","name":"_eventId"})["value"]
rmShown = bshtml.find("input",attrs={"type":"hidden","name":"rmShown"})["value"]

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Content-Length':'172',
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
data = {
    # 替换成自己登录的用户名和密码
    # 'username':'',
    # 'password':'',
    'lt':lt,
    'dllt':dllt,
    'execution':execution,
    '_eventId':_eventId,
    'rmShown':rmShown,
}
print(data)

rep2 = session.post(url,data=data,headers=headers)
rep2.encoding = 'utf-8'
print(rep2.text)
with open('myWiseduCom.txt','w+',encoding='utf-8') as f:
    f.write(rep2.text)
