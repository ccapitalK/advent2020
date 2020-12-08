#!/usr/bin/env python3

values = set()

with open('input', 'r') as f:
    lines = f.read().split('\n')
    for line in lines:
        if line == '':
            continue
        v = int(line)
        if (2020-v) in values:
            print(v, '*', 2020 - v, '=', v*(2020-v))
        values.add(v)
