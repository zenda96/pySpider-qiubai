#!/usr/bin/env python3

import sys
import glob
import os

input_dir = sys.argv[1]

# glob + os 读取输入的整个目录
for txt in glob.glob(os.path.join(input_dir,"*.txt")):
    with open(txt,'r') as f:
        print(f.readlines())