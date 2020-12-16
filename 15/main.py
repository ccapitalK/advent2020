#!/usr/bin/env python3

# https://github.com/SerenityOS/serenity/issues/4417
# gcc is broken in serenityos pending a non-trivial fix, so we are doing today in python :/

from time import sleep
import re

with open('input', 'r') as f:
    data = f.read()

arr = [int(x) for x in data.split(',')]

def solve(index):
    if index < len(arr):
        return arr[index]
    x = arr[-1]
    seen = {x: i for (i, x) in enumerate(arr[:-1])}
    for pos in range(len(arr), index):
        v = pos - seen[x] - 1 if x in seen else 0
        seen[x] = pos - 1
        x = v
    return x

print("Part 1:", solve(2020))
print("Part 2:", solve(30000000))
