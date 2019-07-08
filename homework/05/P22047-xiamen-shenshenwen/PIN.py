"""
【二：本周作业】请同学们于下周天晚上10点前，将作业上传至GitHub；
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

lst1 = []
lst2 = []
for _ in range(100):
    tmp_PIN = random.sample(string.ascii_letters + string.digits, 6)
    for _ in range((len(tmp_PIN))):
        for i in range(3):
            lst1.append(random.randint(0, 255))
        lst2.append(lst1)
        lst1 = []
    if len(lst2) == len(tmp_PIN):
        PIN = dict(zip(tmp_PIN, lst2))
        lst2 = []
    print(PIN)



"""
考虑下颜色的显示，参考P22012-beijing-liyinkai
"""