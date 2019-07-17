#!/usr/bin/env python
# coding:utf-8
# @author: fulijun
# @date: 2019-07-16

'''
使用正则序列化。
    text = 'foo = 23 + 42 * 10' 
将字符串像下面这样转换为序列对：
    tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')] 
'''

import re

# 定义正则匹配元字符
tokens_list = [('NAME', '[a-zA-Z]+'),
               ('EQ', '\='),
               ('NUM', '\d+'),
               ('PLUS', '\+'),
               ('TIMES', '\*')
              ]

# 定义测试字符串
text = '''foo = 23 + 42 * 10, 
          bar = 50 * 2 + 3,
          test = 0.62 + -3 + 10000    # 不支持
       '''

# 正则表达式，使用|连接，表示匹配每个|左边或者右边的正则表达式，re.M表示采用多行匹配模式
reg_patterns = re.compile('|'.join(r'(?P<%s>%s)' % pattern for pattern in tokens_list), re.M)

# 搜索字符串，返回一个顺序访问每一个Match对象的迭代器
for reg_pattern in re.finditer(reg_patterns, text):
    # 打印序列对
    print([(reg_pattern.lastgroup, reg_pattern.group())], end=',')
