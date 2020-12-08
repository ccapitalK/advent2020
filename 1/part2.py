#!/usr/bin/env python3

seen = {}

with open('input', 'r') as f:
    values = [int(x) for x in f.read().split('\n') if x != '']
    n = len(values)
    for (i, v) in enumerate(values):
        seen.setdefault(v, set()).add(i)
    for i in range(n-2):
        for j in range(i+1, n-1):
            a, b = values[i], values[j]
            diff = 2020 - a - b
            if diff in seen:
                for k in seen[diff]:
                    if k != i and k != j:
                        v = values[k]
                        print(a, b, v, a*b*v)
