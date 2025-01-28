import bisect
import random
import sys

haystack = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
needles = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = "{0:2d} @ {1:2d}    {2}{0:<2d}"

def demo(bisect_fn):
    for needle in reversed(needles):
        position = bisect_fn(haystack, needle)
        offset = position * "  |"
        print(ROW_FMT.format(needle, position, offset))

size = 7

my_list = []
for i in range(size):
    new_item = random.randrange(size * 2)
    bisect.insort(my_list, new_item)
    print("%2d ->" % new_item, my_list)

if __name__ == "__main__":
    if sys.argv[-1] == "left":
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print("DEMO:", bisect_fn.__name__)
    print("haystack ->", " ".join("%2d" % n for n in haystack))
    demo(bisect_fn)

