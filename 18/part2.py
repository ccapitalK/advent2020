#!/usr/bin/env python3

# https://github.com/SerenityOS/serenity/issues/4417
# gcc is broken in serenityos pending a non-trivial fix, so we are doing today in python :/

from time import sleep
import re

with open('input', 'r') as f:
    data = f.read()

lines = (x for x in data.split('\n') if x != '')

def visit_a(line):
    # print('A', line)
    return sum(int(x) for x in line.split('+'))

def visit_m(line):
    # print('M', line)
    prod = 1
    for x in line.split('*'):
        prod *= visit_a(x)
    return str(prod)

def visit_e(line):
    # print('E', line)
    i = 0
    rewritten = ''
    while i < len(line):
        if line[i] == '(':
            op = 1
            end = i + 1
            while op > 0:
                if line[end] == '(':
                    op += 1
                elif line[end] == ')':
                    op -= 1
                end += 1
            rewritten += visit_e(line[i+1:end-1])
            i = end
        else:
            rewritten += line[i]
            i += 1
    return visit_m(rewritten)

ans = 0
for line in lines:
    ans += int(visit_e(line.replace(' ', '')))

print(ans)
