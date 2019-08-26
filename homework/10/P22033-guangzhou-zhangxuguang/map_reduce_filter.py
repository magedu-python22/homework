from collections import Iterable


"""
map简单实现
"""

def my_map(func, seq):
    if isinstance(seq, Iterable):
        for i in seq:
            yield func(i)
    else:
        raise Exception("Iterable not is Iterable")

def fn(x):
    return x * x

ret = my_map(fn, [1, 2, 3, 4, 5, 6])
print(list(ret))

"""
reduce简单实现
"""

def my_reduce(func, seq):
    if isinstance(seq, Iterable):
        for i,j in enumerate(seq):
            if i == 0:
                result = j
                continue
            result = func(j,result)
        return result
    else:
        raise Exception("Iterable not is Iterable")

def fn(x,y):
    return x+y

ret = my_reduce(fn, [1, 3, 5, 7, 9])
print(ret)


"""
filter简单实现
"""

def my_filter(func, seq):
    if isinstance(seq, Iterable):
        new_list = []
        for i in seq:
            if func(i):
                new_list.append(i)
        return new_list
    else:
        raise Exception("Iterable not is Iterable")

def fn(n):
    return n % 2 == 1

ret = my_filter(fn, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15])
print(ret)
