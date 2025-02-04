import time
import random

# We try to compare the performance of lists, dicts and sets in finding the needles in haystack

HAYSTACK_SIZE = 10_000
NEEDLE_SIZE = 1000

# Create data structures
haystack = list(range(HAYSTACK_SIZE))
needles = random.sample(range(HAYSTACK_SIZE), NEEDLE_SIZE)

haystack_list = haystack
haystack_set = set(haystack)
haystack_dict = dict.fromkeys(haystack)

# Test list performance
start = time.perf_counter()
found = 0
for n in needles:
    if n in haystack_list:
        found += 1
list_time = time.perf_counter() - start



# Test set performance
start = time.perf_counter()
found = 0
for n in needles:
    if n in haystack_set:
        found += 1
set_time = time.perf_counter() - start


# Test dict performance
start = time.perf_counter()
found = 0
for n in needles:
    if n in haystack_dict:
        found += 1
dict_time = time.perf_counter() - start

print(f'List time: {list_time:.6f}')
print(f'Set time:  {set_time:.6f}')
print(f'Dict time: {dict_time:.6f}')