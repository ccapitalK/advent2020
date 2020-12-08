#!/usr/bin/env python3

import itertools
import re

with open('input', 'r') as f:
    data = f.read()

lines = [x for x in data.split('\n')]

best, x, y = 0, 0, 0

s = 0
seen = None
for line in lines:
    if line == '':
        print(seen)
        s += len(seen)
        seen = None
    else:
        curr = set(x for x in line)
        if seen is None:
            seen = curr
        else:
            seen = seen.intersection(curr)
print(s)
