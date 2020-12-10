#!/usr/bin/env python3

import itertools
import re

with open('input', 'r') as f:
    data = f.read()

lines = [x for x in data.split('\n')]

best, x, y = 0, 0, 0

s = 0
seen = set()
for line in lines:
    if line == '':
        print(seen)
        s += len(seen)
        seen = set()
    for x in line:
        seen.add(x)
print(s)
