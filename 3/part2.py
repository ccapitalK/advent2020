#!/usr/bin/env python3

with open('input', 'r') as f:
    data = f.read()

lines = [x for x in data.split('\n') if x != '']

prod = 1
for (inc, incy) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    x, y = 0, 0
    count = 0
    while y < len(lines):
        line = lines[y]
        if line[x % len(line)] == '#':
            count += 1
        x += inc
        y += incy
    prod *= count

print(prod)
