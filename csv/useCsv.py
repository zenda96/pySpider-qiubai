#-*- coding:utf-8 -*-
#!/usr/bin/env python3

import sys
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file,'r',encoding='utf-8') as csv_in_file:
    with open(output_file,'w',encoding='utf-8') as csv_out_file:
        filereader = csv.reader(csv_in_file,delimiter=',')
        filewriter = csv.writer(csv_out_file,delimiter=',')
        for row in filereader:
            print(row)
            filewriter.writerow(row)
