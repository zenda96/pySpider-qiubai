#-*- coding:utf-8 -*-
#!/usr/bin/env python3

import sys
import csv 
import sqlite3

input_file = sys.argv[1]

con = sqlite3.connect('supplier.db')
c = con.cursor
create_table = """ 
    CREATE TABLE IF NOT EXISTS supplier(
        name VARCHAR(20),
        number VARCHAR(20),
        cost FLOAT,
        data DATE
    )
"""
con.execute(create_table)
con.commit()
#读取CSV文件
file_reader = csv.reader(open(input_file,'r'),delimiter=',')
header = next(file_reader,None)
for row in file_reader:
    print(row)
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    # print(data)
    con.execute("INSERT INTO supplier VALUES (?,?,?,?)",data)
    con.commit()
    #查询
    output = con.execute("SELECT * FROM supplier")
    rows = output.fetchall()
    for row in rows:
        output = []
        for column_index in range(len(row)):
            output.append(str(row[column_index]))
        # print(output)
