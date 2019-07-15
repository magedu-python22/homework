#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Miki
# Date : 2019/7/15 19:20
import re

"""
使用正则序列化。
    text = 'foo = 23 + 42 * 10'
    将字符串像下面这样转换为序列对：
     tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
"""


def tokenize(code):
    tokens = []
    token_specification = [
        ('NAME', '[a-z]+'),
        ('EQ', r'='),
        ('NUM', r'\d+'),
        ('PLUS', r'\+'),
        ('MINUS', r'-'),
        ('TIMES', r'\*'),
        ('NEWLINE', r'\n'),
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == 'NEWLINE':
            if mo.end() == 1:
                continue
            yield tokens
            tokens = []
        else:
            tokens.append((kind, value))
            if mo.end() == len(code):
                yield tokens


text = '''
foo = 23 + 42 * 10 
foo1 = 23 - 214 + 800
'''
for token in tokenize(text):
    print(token)

text = 'foo = 23 + 42 * 10'
for token in tokenize(text):
    print(token)