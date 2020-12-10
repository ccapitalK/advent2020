#!/usr/bin/env python3

import re
from typing import List, Optional

class BagRule:
    def __init__(self, container, contained, amount):
        self.container = container
        self.contained = contained
        self.amount = amount

    def __repr__(self):
        return f"{self.container} -> {self.contained}: {self.amount}"

class Bag:
    def __init__(self, name):
        self.name = name
        self.contained = {}
        self.containers = {}

    def add_contained(self, child, amount):
        self.contained[child] = amount

    def add_container(self, parent, amount):
        self.containers[parent] = amount

class BagGraph:
    def __init__(self):
        self.bags = {}

    def add_bag(self, bag_name):
        if bag_name not in self.bags:
            self.bags[bag_name] = Bag(bag_name)

    def add_rule(self, rule):
        self.add_bag(rule.container)
        self.add_bag(rule.contained)
        container = self.bags[rule.container]
        contained = self.bags[rule.contained]
        amount = rule.amount
        container.add_contained(contained, amount)
        contained.add_container(container, amount)

    def num_containers(self, bag):
        seen = set()
        stack = [bag]
        while len(stack) > 0:
            bag = stack.pop()
            seen.add(bag)
            for parent in bag.containers.keys():
                if parent not in seen:
                    stack.append(parent)
        return len(seen)

    def total_contained(self, bag):
        contained = (x for x in bag.contained.items())
        return 1 + sum(amount * self.total_contained(bag) for (bag, amount) in contained)

def parse_rules(line: str) -> List[BagRule]:
    line_pattern: str = '^([a-z ]+) bags contain (.*)$'
    inner_pattern: str = '([0-9]+) ([a-z ]+) bag'
    potential_match: Optional[re.Match] = re.match(line_pattern, line)
    if potential_match is None:
        raise ValueError(f"Could not parse line \"{line}\"")
    match: re.Match = potential_match
    container: str = match.group(1)
    rest: str = match.group(2)
    rules = []
    if 'no other bags' not in rest:
        for m in re.findall(inner_pattern, rest):
            contained = m[1]
            amount = int(m[0])
            new_rule = BagRule(container, contained, amount)
            rules.append(new_rule)
    return rules

def read_input(file_name: str) -> List[BagRule]:
    with open(file_name, 'r') as f:
        data = f.read()
    lines: List[str] = [x for x in data.split('\n') if x != '']
    return [rule for line in lines for rule in parse_rules(line)]

graph = BagGraph()
for rule in read_input('input'):
    graph.add_rule(rule)

print("Part 1:", graph.num_containers(graph.bags['shiny gold']) - 1)

print("Part 2:", graph.total_contained(graph.bags['shiny gold']) - 1)
