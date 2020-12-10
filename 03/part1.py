#!/usr/bin/env python3

with open('input', 'r') as f:
    data = f.read()

lines = [x for x in data.split('\n') if x != '']

x = 0
count = 0
for line in lines:
    if line[x % len(line)] == '#':
        count += 1
    x += 3

print(count)
