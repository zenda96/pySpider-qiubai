#-*- coding:utf-8 -*-
#!/usr/bin/env python3

#创建sqlite3内存数据库
#创建带有4个属性的sales表
import sqlite3
#表示在当前目录建库   :memory: 在内存建临时库 
con = sqlite3.connect('test.db')
query = """ 
            CREATE TABLE sales
                (customer VARCHAR(20),
                product VARCHAR(40),
                amount FLOAT,
                date DATE);
        """
#执行语句
con.execute(query)
#保存修改
con.commit()

#在表中插入数据
data = [('zenda','notepad',2.5,'2018-02-26'),
        ('zendaa','notepad',2.5,'2018-02-26'),
        ('zendaaa','notepad',2.5,'2018-02-26')]
statement = "INSERT INTO sales VALUES(?,?,?,?)"  #问号作为占位符
con.executemany(statement,data)
con.commit()

#查询
cursor = con.execute('SELECT * FROM sales')
rows = cursor.fetchall()

#计算查询结果中行的数量
row_counter = 0
for row in rows:
    print(row)
    row_counter+=1
print(row_counter)
