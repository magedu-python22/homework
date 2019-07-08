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

set1 = set()
num1 = 0
while num1 < 100:
    set1.add(''.join(random.sample(string.ascii_letters + string.digits,6)))
    num1 = len(set1)

for I in set1:
    dict1 = {}
    set2 = set()
    num2 = 0
    while num2 < 6:
        set2.add(tuple(random.sample([x for x in range(256)],3)))
        num2 = len(set2)
    for k in I:
        dict1[k] = set2.pop()
    print(dict1)


"""
考虑下颜色的显示，参考P22012-beijing-liyinkai
"""