# !/usr/bin/env python
# -*- coding:utf-8 -*-
import itchat

itchat.auto_login(enableCmdQR=2)
friends = itchat.get_friends(update=True)[:]
female = male = other = 0
province = {}
# print(friends)
for friend in friends:
    sex = friend['Sex']
    if sex == 1:
        male +=1
    elif sex ==2:
        female +=1
    else:
        other +=1
    province[friend['Province']] = province.get(friend['Province'],0)+1
print("male:%d  female%d" %(male,female))
for key in province:
    print("%s : %s 人" %(key,province[key]))
# print(province)
#itchat.send('Hello, filehelper', toUserName='filehelper')
@itchat.msg_register('Text')
def text_reply(msg):
    # 返回同样的文本消息
    return '你是小可爱！！'
# 获取自己的UserName
myUserName = itchat.get_friends(update=True)[0]["UserName"]
itchat.run()