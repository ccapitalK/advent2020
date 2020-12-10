#!/usr/bin/env python3

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
            adj.setdefault(sub, []).append((a, num))
            print(a, m[0], m[1])

seen = set()

def dfs(node):
    if node in seen:
        return
    seen.add(node)
    print(node)
    for x in adj[node]:
        dfs(x[0])

dfs('shiny gold')
print(len(seen)-1)
