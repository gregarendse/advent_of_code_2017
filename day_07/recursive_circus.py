from typing import List


class Program(object):
    name: str
    weight: int
    children = []

    def __init__(self, name: str = None, children=None, weight: int = None):
        if children is None:
            children = []
        self.name = name
        self.children = children
        self.weight = weight


program_map = {}
children = set()
with open('input') as file:
    for line in file.readlines():
        parts: List[str] = line.split('->')

        first_parts: List[str] = parts[0].split()

        program = Program(
            name=str(first_parts[0]),
            weight=int(first_parts[1].replace('(', '').replace(')', ''))
        )

        if len(parts) > 1:
            program.children = [i.strip() for i in parts[1].split(',')]

        program_map[program.name] = program

        for child in program.children:
            children.add(child)

root = None
for key in program_map.keys():
    if key not in children:
        print(key)
        root = key

# for root in program_map.keys():
#     break

def calculate_weight(input: program) -> int:
    weight = input.weight

    for child in [program_map.get(i) for i in input.children]:
        weight = weight + calculate_weight(child)

    return weight

def find_inbalance(input: program):
    weights = {}
    programs = {}
    for program in [program_map.get(i) for i in program_map.get(input).children]:
        weight = calculate_weight(program)
        if weights.get(weight) is None:
            weights[weight] = []
        weights[weight].append(program.name)
    print(weights)

    for i, key in enumerate(weights):
        if len(weights[key]) == 1:
            find_inbalance(weights[key][0])




find_inbalance(root)

if False:
    weights = {}
    # dtacyn (42) -> xvuxc, eyyrn, udtsgjk, zprkrrn, rhhdc, rtdpm
    print(root)
    for program in [program_map.get(i) for i in program_map.get(root).children]:
        print('\t', program.name, program.weight)
        weight = int(program.weight)

        # xvuxc (39164) -> nieyygi, hmcjz, ceizm
        for child in [program_map.get(i) for i in program.children]:
            print('\t\t', child.name, child.weight)
            weight = weight + int(child.weight)

        if weights.get(weight) is None:
            weights[weight] = 0

        weights[weight] = weights[weight] + 1
        print(weight)

    print(weights)

# for program in program_map.values():
#     balances = {}
#     for child in [program_map.get(i) for i in program.children]:
#         weight = int(child.weight)
#
#         for inner_child in [program_map.get(i) for i in child.children]:
#             weight = weight + int(inner_child.weight)
#
#         if balances.get(weight) is None:
#             balances[weight] = 0
#
#         balances[weight] = balances[weight] + 1
#
#
#         # print('{value} -> {weight} + {children}'.format(value=program.name, weight=child.name,
#         #                                                 children=[i for i in child.children]))
#     if len(balances.keys()) == 2:
#         print(balances)
