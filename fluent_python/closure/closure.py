## Closures

class Averager():
    def __init__(self):
        self.series = []
    
    def __call__(self, new_value):
        self.series.append(new_value)

        return sum(self.series)/len(self.series)

avg = Averager()

print(avg(6))
print(avg(8))


def make_average():
    series = []

    def averager(new_value):
        print(series)

        series.append(new_value)

        return sum(series)/len(series)
    
    return averager

avg = make_average()

print(avg(6))
print(avg(8))


# Using nonlocal variables to refactor the above code
def make_average_nonlocal():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total

        count += 1
        total += new_value

        return total/count
    
    return averager
    
avg = make_average_nonlocal()

print(avg(6))
print(avg(8))

import time
import functools

def clock(func):
    functools.wraps(func)
    def clocked(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        func_name = func.__name__
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f'{func_name}({signature}) took {elapsed:.8f}s')
        return result
    return clocked

@clock
def test_function(seconds):
    time.sleep(seconds)
    return 'done'

test_function(1.5)

@functools.lru_cache()
@clock
def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

fibo(8)