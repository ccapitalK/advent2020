#!/usr/bin/env python3

# https://github.com/SerenityOS/serenity/issues/4417
# gcc is broken in serenityos pending a non-trivial fix, so we are doing today in python :/

from time import sleep
import re

with open('input', 'r') as f:
    data = f.read()

lines = (x for x in data.split('\n'))
valid = [set() for x in range(1000)]
names = set()

for line in lines:
    if line == '':
        break
    [rule_name, ranges] = line.split(':')
    names.add(rule_name)
    ranges = ranges.split(' ')
    for r in (ranges[1], ranges[3]):
        [start, end] = [int(x) for x in r.split('-')]
        for i in range(start, end+1):
            valid[i].add(rule_name)

for line in lines:
    if line == '':
        break
    if line[0] != 'y':
        my_ticket = [int(x) for x in line.split(',')]

N = len(my_ticket)
next(lines)

num_error = 0
tickets = []

for line in lines:
    if line == '':
        break
    nearby_ticket = [int(x) for x in line.split(',')]
    is_valid = True
    for x in nearby_ticket:
        if len(valid[x]) == 0:
            is_valid = False
            num_error += x
    if is_valid:
        tickets.append(nearby_ticket)

print('Part 1:', num_error)

fields = [set(names) for _ in range(N)]

for ticket in tickets:
    for (i, x) in enumerate(ticket):
        fields[i] = fields[i].intersection(valid[x])

field_names = [None for x in range(N)]

for _ in range(N):
    for j in range(N):
        if len(fields[j]) == 1:
            name = fields[j].pop()
            field_names[j] = name
            for k in range(N):
                fields[k].discard(name)
            break

dep_prod = 1
for i in range(N):
    if field_names[i].startswith('departure'):
        dep_prod *= my_ticket[i]

print("Part 2:", dep_prod)
