class Instruction(object):
    def __init__(self, registry_name: str = None,
     action: str = None,
      modifier: int = None,
       compare_registry: str = None,
        compare_action: str = None,
         compare_value: str = None):
        self.registry_name = registry_name
        self.action = action
        self.modifier = modifier
        self.compare_registry = compare_registry
        self.compare_value = compare_value
        self.compare_action = compare_action


with open('day_08/input') as file:
    lines = file.readlines()

instructions = []
registries = {}

for line in lines:
    parts = line.split()
    print(parts)
    instructions.append(Instruction(
        str(parts[0]),
        str(parts[1]),
        int(parts[2]),
        str(parts[4]),
        str(parts[5]),
        int(parts[6])
        ))
    if registries.get(str(parts[0])) == None:
        registries[str(parts[0])] = 0

working_max = 0
for instruction in instructions:
    if instruction.compare_action == '>':
        if not (registries[instruction.compare_registry] > instruction.compare_value):
            continue
    elif instruction.compare_action == '<':
        if not (registries[instruction.compare_registry] < instruction.compare_value):
            continue
    elif instruction.compare_action == '>=':
        if not (registries[instruction.compare_registry] >= instruction.compare_value):
            continue
    elif instruction.compare_action == '<=':
        if not (registries[instruction.compare_registry] <= instruction.compare_value):
            continue
    elif instruction.compare_action == '==':
        if not (registries[instruction.compare_registry] == instruction.compare_value):
            continue
    elif instruction.compare_action == '!=':
        if not (registries[instruction.compare_registry] != instruction.compare_value):
            continue
    else:
        print('we shouldnt get here', instruction.compare_action)

    if instruction.action == 'inc':
        registries[instruction.registry_name] = int(registries[instruction.registry_name]) + int(instruction.modifier)
    elif instruction.action == 'dec':
        registries[instruction.registry_name] = int(registries[instruction.registry_name]) - int(instruction.modifier)

    if max(registries.values()) > working_max:
        working_max = max(registries.values())

print(registries)
print('final max: ', max(registries.values()))
print('working max: ', working_max)

