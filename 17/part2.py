#!/usr/bin/env python3

# https://github.com/SerenityOS/serenity/issues/4417
# gcc is broken in serenityos pending a non-trivial fix, so we are doing today in python :/

from time import sleep
import re

with open('input', 'r') as f:
    data = f.read()

lines = (x for x in data.split('\n') if x != '')

def neighbours(point, centre=False):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if centre or dx != 0 or dy != 0 or dz != 0 or dw != 0:
                        yield (point[0] + dx, point[1] + dy, point[2] + dz, point[3] + dw)

grids = [set()]

for (y, line) in enumerate(lines):
    for (x, c) in enumerate(line):
        if c == '#':
            grids[0].add((x, y, 0, 0))

def next_grid(prev):
    grid = set()
    possible = set(cand for pos in prev for cand in neighbours(pos, True))
    for cand in possible:
        if cand in prev:
            if sum(x in prev for x in neighbours(cand)) in (2, 3):
                grid.add(cand)
        elif sum(x in prev for x in neighbours(cand)) == 3:
            grid.add(cand)
    return grid

for i in range(6):
    grids.append(next_grid(grids[i]))
    
print(len(grids[6]))
