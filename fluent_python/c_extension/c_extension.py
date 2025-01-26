# We try to compare three different setups for running a code and see the performance difference.
# One is with pure python, one is with numpy and one is with c extension.

# The below code is the pure python code
import time
import numpy as np

def pure_python_sum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

n = 10000000
start = time.time()
print(pure_python_sum(n))
print("Time taken for pure python code: ", time.time() - start)

# The below code is the numpy code
def numpy_sum(n):
    return np.sum(np.arange(n+1))

start = time.time()
print(numpy_sum(n))
print("Time taken for numpy code: ", time.time() - start)


# The below code is the c extension code
import ctypes
import os

# Load the shared library into c types.
current_dir = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(current_dir, "withc.so")
sum_cal = ctypes.CDLL(lib_path)

sum_cal.calculate_sum.argtypes = [ctypes.c_int]
sum_cal.calculate_sum.restype = ctypes.c_int

def c_sum(n):
    return sum_cal.calculate_sum(n)

start = time.time()
print(c_sum(n))
print("Time taken for c extension code: ", time.time() - start)

# The below lines are the outputs of the above code

# Time taken for pure python code:  0.6376156806945801
# Time taken for numpy code:  0.02468729019165039
# Time taken for c extension code:  0.03383231163024902

# The above code shows that the numpy code is the fastest and the c extension code is the second fastest