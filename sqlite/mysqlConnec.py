#-*- coding:utf-8 -*-
#!/usr/bin/env python3

import sys
import csv
import MySQLdb
from datetime import datetime,date

input_file = sys.argv[1]
output_file = sys.argv[2]
#连接sql数据库
con = MySQLdb.connect(host='localhost',port=3306,db='a',user='root',password='root')
c=con.cursor()
#像表中插入数据
file_reader = csv.reader(open(input_file,'r'))
file_writter = csv.writer(open(output_file,'w'))
header = next(file_reader)
for row in file_reader:
    data=[]
    for column_index in range(len(header)):
        data.append(str(row[column_index]))
    print(data)
    c.execute("""insert into aa values (%s,%s,%s);""",data)
con.commit()
print("插入成功")
#查询
c.execute("select * from aa")
rows=c.fetchall()
for row in rows:
    row_list = []
    for column_index in range(len(row)):
        row_list.append(str(row[column_index]))
    #写入另外一个文件
    file_writter.writerow(row)
    print(row_list)
