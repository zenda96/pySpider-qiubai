#-*- coding:utf-8 -*-
#!/usr/bin/env python3

#读写单个excel文件  只能写.xls
import sys
from xlrd import open_workbook
from xlwt import Workbook
input_file = sys.argv[1]
output_file = sys.argv[2]
#实例化一个 xlwt Workbook对象  并新建一个sheet
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('b')
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('Sheet1')
    for i in range(worksheet.nrows):
        for j in range(worksheet.ncols):
            output_worksheet.write(i,j,worksheet.cell_value(i,j))
output_workbook.save(output_file)

