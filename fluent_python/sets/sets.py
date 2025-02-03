# Count occurence of needles in haystack using sets
haystack = [1, 23, 42, 65, 87, 2, 15, 33, 98, 54, 7, 11, 89, 36, 71, 45, 19, 83, 60, 27]
needles = [23,7,19]

found = len(set(needles) & set(haystack))
print(found)

# using intersection
found = len(set(needles).intersection(haystack))
print(found)


from dis import dis
dis("{1}")
print("-----------------------------------------")
dis("set([1])")

# Set comprehension
from unicodedata import name
set_comp = {chr(i) for i in range(32,256) if "SIGN" in name(chr(i),'')}
print(set_comp)