#!/usr/bin/env python3

# https://github.com/SerenityOS/serenity/issues/4417
# gcc is broken in serenityos pending a non-trivial fix, so we are doing today in python :/

from time import sleep
import re

with open('input', 'r') as f:
    data = f.read()

arr = [int(x) for x in data.split(',')]

def solve(index):
    if index <= len(arr):
        return arr[index - 1]
    current_num = arr[-1]
    seen = {x: i for (i, x) in enumerate(arr[:-1])}
    for pos in range(len(arr), index):
        new_num = pos - seen[current_num] - 1 if current_num in seen else 0
        seen[current_num] = pos - 1
        current_num = new_num
    return current_num

print("Part 1:", solve(2020))
print("Part 2:", solve(30000000))
