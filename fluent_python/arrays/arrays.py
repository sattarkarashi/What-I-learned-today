from array import array
from random import random

# Lots of times we can use arrays to solve problems instead of lists. Here are some examples.
floats = array('d', (random() for _ in range(10**7)))
print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)

print(floats2[-1])
print(floats2 == floats)

# Memoryview
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))

memv_oct = memv.cast('B')
print(memv_oct.tolist())

memv_oct[5] = 4
print(numbers)
