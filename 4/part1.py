#!/usr/bin/env python3

import re

with open('input', 'r') as f:
    data = f.read()

lines = data.split('\n')

passports = []
item = {}

for line in lines:
    if line == '':
        if len(item) > 0:
            passports.append(item)
            item = {}
    else:
        entries = line.split(' ')
        for entry in entries:
            [k, v] = entry.split(':')
            item[k] = v

if len(item) > 0:
    passports.append(item)

print(passports)

def is_valid(x):
    validators = {
        'byr': '19[2-9][0-9]|200[0-2]',
        'iyr': '20(1[0-9]|20)',
        'eyr': '20(2[0-9]|30)',
        'hgt': '1([5-8][0-9]|9[0-3])cm|(59|7[0-6]|6[0-9])in',
        'hcl': '#[0-9a-f]{6}',
        'ecl': 'amb|blu|brn|gry|grn|hzl|oth',
        'pid': '[0-9]{9}'
    }
    for (field, pattern) in validators.items():
        if field not in x:
            return False
        if re.fullmatch(pattern, x[field]) is None:
            return False
    return True

valid = [x for x in passports if is_valid(x)]
print(len(valid))
