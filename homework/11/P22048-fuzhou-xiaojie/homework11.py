import datetime
import time
from functools import wraps

def decorator(times=1, date=lambda name, times:print('{} 的运行时间是 {:.2f}s'.format(name, times))):
    def _decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            if delta > times:
                # print('{} 执行了 {}'.format(fn.__name__, delta))
                date(fn.__name__, delta)
                print('{} 的结果是 {}'.format(fn.__name__, ret))
            # print(start)
            return ret
        return wrapper
    return _decorator



@decorator()
def add(x, y, z):
    time.sleep(2)
    return x + y + z


add(1, 2, 3)