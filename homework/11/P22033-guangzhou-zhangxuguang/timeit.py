import datetime
import time


# 1. 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def timeit(func):
    def wapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = func(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print('time used:', delta)
        return ret
    return wapper


@timeit
def test(x, y):
    time.sleep(1)
    return x + y

print(test(3, 4))


# 2. 请设计一个decorator，它可作用于任何函数上，要求可以接受一个int作为参数，如果该函数的执行时间大于int传递的时间话，请打印改函数名字和执行时间
def timeit(int, func=lambda name, delta: print('function {} took {}s'.format(name, delta))):
    def _timeit(fn):
        def wapper(*args, **kwargs):
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            if delta > int:
                func(fn.__name__, delta)
            return ret
        return wapper
    return _timeit


@timeit(2)
def test(x, y):
    time.sleep(3)
    return x + y

print(test(3, 4))
