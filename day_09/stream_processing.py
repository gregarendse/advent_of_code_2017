import re

with open('day_09/input') as file:
    source = file.read()


def score(input: str) -> [int, int]:
    source = re.sub(r'!.', '', input)
    # source = input.replace('!!', '')            # Remove double excludes
    # source = source.replace('<>', '')
    # source = re.sub(r'<.*?[^!]>', '', source)   # Remove garbage
    [source, count] = garbage_count(input=source)
    level = 0
    level_count = 0
    for character in source:
        if character == '{':
            level = level + 1
            level_count = level_count + level
        elif character == '}':
            level = level - 1

    # print(input, level_count)
    return [level_count, count]


def garbage_count(input: str, count: int = 0) -> [str, int]:
    open: bool = False
    position = 0
    for i, character in enumerate(input):
        if not open and character == '<':
            open = True
            position = i
        elif open and character == '>':
            count = count + (len(input[position + 1: i]))
            return garbage_count(input=str(input[:position]) + str(input[i + 1:]), count=count)

    return [input, count]


def remove(input: str) -> str:
    open: bool = False
    position = 0
    for i, character in enumerate(input):
        if not open and character == '<':
            open = True
            position = i

        if open and character == '>':
            open = False
            return remove(str(input[:position]) + str(input[i + 1:]))

    return input


"""
Tests:
    {}, score of 1.
    {{{}}}, score of 1 + 2 + 3 = 6.
    {{},{}}, score of 1 + 2 + 2 = 5.
    {{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
    {<a>,<a>,<a>,<a>}, score of 1.
    {{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
    {{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
    {{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.
    
Part II
    <>, 0 characters.
    <random characters>, 17 characters.
    <<<<>, 3 characters.
    <{!>}>, 2 characters.
    <!!>, 0 characters.
    <!!!>>, 0 characters.
    <{o"i!a,<{i<a>, 10 characters.
"""
assert (score('<>') == [0, 0])
assert (score('<random characters>') == [0, 17])
assert (score('<<<<>') == [0, 3])
assert (score('<{!>}>') == [0, 2])
assert (score('<!!>') == [0, 0])
assert (score('<!!!>>') == [0, 0])
assert (score('<{o"i!a,<{i<a>') == [0, 10])

# assert score('{}') == 1
# assert score('{{{}}}') == 6
# assert score('{{},{}}') == 5
# assert score('{{{},{},{{}}}}') == 16
# assert score('{<a>,<a>,<a>,<a>}') == 1
# assert score('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
# assert score('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
# assert score('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3

#   5489 - too low
#   7183 - too low?
[score, count] = score(source)
print('score: ', score)
assert score == 7616
# 622526 too high
#   4303 too high
print('count: ', count)
