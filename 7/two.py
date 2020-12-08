#!/usr/bin/env python3

from functools import cache
import itertools
import re

with open('input', 'r') as f:
    data = f.read()

lines = [x for x in data.split('\n') if x != '']

best, x, y = 0, 0, 0

rules = []

pat = '^([a-z ]+) bags contain(.*)$'
pat2 = '([0-9]+) ([a-z ]+) bags?'
adj = {}

for line in lines:
    m = re.match(pat, line)
    g = m.groups()
    a = g[0]
    adj.setdefault(a, [])
    rest = g[1]
    if rest != ' no other bags.':
        for m in re.findall(pat2, rest):
            num = int(m[0])
            sub = m[1]
            adj.setdefault(a, []).append((sub, num))
            print(a, m[0], m[1])

@cache
def dfs(node):
    return 1 + sum(dfs(x[0]) * x[1] for x in adj[node])

print(dfs('shiny gold') - 1)
