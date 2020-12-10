#!/usr/bin/env python3

with open('input', 'r') as f:
    data = f.read()

lines = [x for x in data.split('\n') if x != '']

out = 0

for line in lines:
    [a, b] = line.split(':')
    p = b.lstrip()
    [bounds, c] = a.split(' ')
    [l, u] = [int(x) for x in bounds.split('-')]
    if (p[l-1] == c) != (p[u-1] == c):
        out += 1

print(out)
