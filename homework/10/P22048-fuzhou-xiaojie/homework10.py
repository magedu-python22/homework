#   自定义 map， reduce， filter    接受两个参数（fn， iterable）
#     检测iterable 是否为可迭代对象， 如果不是抛出异常  “Iterable not is Iterable”

from collections import Iterable


def add(x, y):
    return x + y

def is_odd(x):
    return  x % 2 == 1

class MyException(Exception):
    pass


class Custom:
    def __init__(self, fn, iterable):
        self.fn = fn
        self.iterable = iterable

    def map(self):
        try:
            if isinstance(self.iterable, Iterable):
                return self.fn(*self.iterable)
            else:
                raise MyException
        except MyException:
            print('Iterable not is Iterable')
    def reduce(self):
        try:
            if isinstance(self.iterable, Iterable):
                result = 0
                for i in self.iterable:
                    result += i
                return result
            else:
                raise MyException
        except MyException:
            print('Iterable not is Iterable')

    def filter(self):
        try:
            if isinstance(self.iterable, Iterable):
                result = []
                for i in self.iterable:
                    if self.fn(i):
                        result.append(i)
                return result
            else:
                raise MyException
        except MyException:
            print('Iterable not is Iterable')



m = Custom(add, [3, 4])
print(m.map())

r = Custom(add, [1, 2, 3, 4, 5])
print(r.reduce())

f = Custom(is_odd, [1, 2, 3, 4, 5, 6, 7])
print(f.filter())