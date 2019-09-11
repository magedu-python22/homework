from datetime import datetime
from functools import wraps
import time


def decorator(times: int):
    def _decorator(fn):
        @wraps(fn)
        def wrap(*args, **kwargs):
            start = datetime.now()
            ret = fn(*args, **kwargs)
            datel = (datetime.now() - start).total_seconds()
            if datel > times:
                print("names:{}, {}s".format(fn.__name__, datel))
            return ret

        return wrap

    return _decorator


@decorator(1)
def add(x, y):
    time.sleep(2)
    return print(x + y)


add(4, 5)

# 符合要求，也加上了wraps了