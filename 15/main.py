#!/usr/bin/env python3

# https://github.com/SerenityOS/serenity/issues/4417
# gcc is broken in serenityos pending a non-trivial fix, so we are doing today in python :/

import re

with open('input', 'r') as f:
    data = f.read()

arr = [int(x) for x in data.split(',')]
seen = {x: i for (i, x) in enumerate(arr[:-1])}

def solve(index):
    while len(arr) < index:
        if (len(arr) % 10000) == 0:
            print('Progress:', len(arr), '/', index)
        x = arr[-1]
        if x in seen:
            v = len(arr) - seen[x] - 1
        else:
            v = 0
        seen[x] = len(arr) - 1
        arr.append(v)
    return arr[index-1]

print("Part 1:", solve(2020))
print("Part 2:", solve(30000000))
