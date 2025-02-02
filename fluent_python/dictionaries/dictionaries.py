# Handling missing keys with setdefault

# An unefficient way to handle missing keys in a dictionary is to use the get method as shown below:
import sys
import re

WORD_RE = re.compile(r'\w+') # \w+ matches one or more word characters
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        print(line_no, line)
        for match in WORD_RE.finditer(line):
            
            word = match.group()
            print(match, word)
            column_no = match.start() + 1
            location = (line_no, column_no)
            # this is ugly; coded like this to make a point
            occurrences = index.get(word, [])
            occurrences.append(location)

            index[word] = occurrences

print(index)

# The above code can be written in a more efficient way using the setdefault method as shown below:
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])


print("=====================================")
# Using defaultdict to handle missing keys
from collections import defaultdict

WORD_RE = re.compile(r'\w+')
index = defaultdict(list)

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            # print(index)
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)
for word in sorted(index, key=str.upper):
    print(word, index[word])