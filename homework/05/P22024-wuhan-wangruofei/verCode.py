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


def GetLetter():
    """
    获取一个由大写字母和数字组成的字符串
    :return: 字符串
    """
    return string.ascii_letters + string.digits

def GetColor():
    """
    获取颜色元组
    :return: 元组
    """
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def VerCode(num):
    """
    num为一个验证码的位数
    :param num:
    :return: 一个num位验证码
    """
    color = []
    List = []
    for i in range(num):
        while 1: #防止颜色重复
            tmp = GetColor()
            if tmp in color:
                continue
            else:
                color.append(tmp)
                List1 = [random.choice(GetLetter()), tmp]
                break
        List.append(List1)
    return List

def main():
    """
    获取100个验证码，并打印
    :return: 100个验证码
    """
    VeriCode = [0 for i in range(100)]
    for i in range(100):
        VeriCode[i] = VerCode(6)
        print(VeriCode[i])
    return VeriCode


if __name__ == '__main__':
    main()