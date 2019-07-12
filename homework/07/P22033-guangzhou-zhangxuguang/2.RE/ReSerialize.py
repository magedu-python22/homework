"""
2.使用正则序列化。
    text = 'foo = 23 + 42 * 10'
    将字符串像下面这样转换为序列对：
     tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
"""

import re


text = 'foo = 23 + 42 * 10'
regex = re.compile("\w+|\S")
result = regex.findall(text)

keys = ['NAME', 'EQ', 'NUM', 'PLUS', 'NUM', 'TIMES', 'NUM']
tokens = list(zip(keys,result))

print(tokens)