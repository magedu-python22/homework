#!/usr/bin/env python
# coding:utf-8
# @author: fulijun
# @date: 2019-06-17

'''
随机生成100个验证码，每个验证码由6个元素构成:
1、要求使用random模块
2、验证码由字母和数字构成
3、要求验证码中的每个元素为一种颜色
提示 颜色可以用数字来表示:一般都是3个 (0, 255)之间的数字来构成的
demo:
Z (19, 157, 229)
2 (239, 10, 145)
Z (145, 142, 244)
M (231, 58, 7)
T (202, 19, 72)
F (182, 136, 237) 
'''

import random
import string

def authCodeGenerator(total_num, code_len):
    # 验证码由字母（包括大写和小写）和数字构成
    code_elements = string.ascii_letters + string.digits
    
    for i in range(total_num):
        # 定义一个存放一组随机验证码的变量，每一次迭代会将其置空
        auth_code = ''
        # 生成total_num个code_len长度的验证码
        code = random.sample(code_elements, code_len)
        # 遍历验证码的每一个元素
        for j in code:
            # 为验证码中的每个元素随机生成一种颜色
            code_color = random.sample([i for i in range(256)], 3)
            # 将验证码每个元素及其颜色拼接为一个整串
            auth_code += '{} {}'.format(j, tuple(code_color))

        # 返回一个生成器对象 
        yield auth_code
            
# 主程序遍历生成器对象，依次打印每一个验证码
for idx,item in enumerate(authCodeGenerator(100, 6), 1):
    print('No {}\t'.format(idx), item)
    