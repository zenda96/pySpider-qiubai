#-*- coding:utf-8 -*-
#!/usr/bim/env python3

import sys 
from xlrd import open_workbook
input_file = sys.argv[1]
workbook = open_workbook(input_file)
#获取默认工作簿的数量以及行列数等
print('Number of workbook:',workbook.nsheets)
for worksheet in workbook.sheets():
    print ('worksheet name',worksheet.name)
    print ('worksheet rows',worksheet.nrows)
    print ('worksheet cols',worksheet.ncols)