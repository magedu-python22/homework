#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Miki
# Date : 2019/7/10 9:16

"""
使用正则序列化。
    text = 'foo = 23 + 42 * 10'
    将字符串像下面这样转换为序列对：
     tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
"""


import pickle
import re
text = 'foo = 23 + 42 * 10'
group = ['NAME', 'EQ', 'NUM', 'PLUS', 'NUM', 'TIMES', 'NUM']
result = re.split('\s', text)
dest = list(zip(group, result))
serialization = pickle.dumps(dest)
print(pickle.loads(serialization))
# with open('week7-1','wb+') as f:
#     pickle.dump(dest,f)
#
# with open('week7-1', 'rb') as f:
#     print(pickle.load(f))
