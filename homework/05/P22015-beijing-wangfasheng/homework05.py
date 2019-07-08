# -*- coding: utf-8 -*-
# @file   : Sort.py
# @author : wfs
# @date   : 2019/06/29
# @version: 1.0
# @desc   :

"""
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
"""

import random
import string

# 生成100个验证码
my_list = []
for i in range(100):
    my_list.append("".join(random.sample(string.ascii_letters + string.digits, 6)))

# 给验证码的每个元素添加颜色
for j in my_list:
    for k in j:
        print(k, tuple(random.sample([n for n in range(256)], 3)))
    print("#"*6)



"""
考虑下颜色的显示，参考P22012-beijing-liyinkai
"""

