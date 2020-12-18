#!/usr/bin/env python3

# https://github.com/SerenityOS/serenity/issues/4417
# gcc is broken in serenityos pending a non-trivial fix, so we are doing today in python :/

from time import sleep
import re

with open('input', 'r') as f:
    data = f.read()

lines = (x for x in data.split('\n') if x != '')

def visit(line):
    print('Visit', line)
    rv = None
    i = 0
    is_mul = False
    while i < len(line):
        c = line[i]
        if line[i] == ' ':
            i += 1
            continue
        elif line[i] == '(':
            (num, l) = visit(line[i+1:])
            if rv is None:
                rv = num
            elif is_mul:
                rv *= num
            else:
                rv += num
            i += l + 2
        elif line[i] == ')':
            return (rv, i)
        elif line[i] == '*':
            i += 1
            is_mul = True
        elif line[i] == '+':
            i += 1
            is_mul = False
        else:
            num = ''
            while i < len(line) and line[i].isdigit():
                num += line[i]
                i += 1
            num = int(num)
            if rv is None:
                rv = num
            elif is_mul:
                rv *= num
            else:
                rv += num
    return (rv, i)

ans = 0
for line in lines:
    ans += visit(line)[0]

print(ans)
