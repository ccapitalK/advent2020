#!/usr/bin/env python3

with open('input', 'r') as f:
    data = f.read()

lines = [x for x in data.split('\n') if x != '']

seen = []

best = 0
for line in lines:
    x, y = 0, 0
    for c in line:
        if c == 'B':
            y = y * 2 + 1
        if c == 'F':
            y = y * 2
        if c == 'R':
            x = x * 2 + 1
        if c == 'L':
            x = x * 2
    i = y * 8 + x
    seen.append(i)
    best = max(best, i)

seen.sort()

for i in range(len(seen)-1):
    if seen[i] + 1 != seen[i+1]:
        print(seen[i] + 1)
