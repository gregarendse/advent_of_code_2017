import math

def spiral_memory(input):
    level = get_level(input)
    print("Level: ", level)
    [lower, upper] = get_bounds(input)
    print("Lower: ", lower)
    off_set = abs((input - 1) % (lower + 1) - (lower + 1) / 2)
    print("Off Set: ", off_set)
    return level + off_set

# [[i, abs((i - 0) % 4 - 2)] for i in range(2, 10)]

# [[i, abs((i - 1) % 2 - 1)] for i in range(2, 10)]     1
# [[i, abs((i - 1) % 4 - 2)] for i in range(10, 26)]    2
# [[i, abs((i - 1) % 6 - 3)] for i in range(26, 49)]    3

# [[i, abs((i - 1) % (2 * input) - input)] for i in range((input * input) + 1, ((input + 2) * (input + 2)) + 1)]

# [[i, abs((i - 1) % (input+1) - (input+1)/2)] for i in range((input * input) + 1, ((input + 2) * (input + 2)) + 1)]

def get_bounds(input):
    sqrt = math.sqrt(input)

    lower = math.floor(sqrt)
    upper = math.ceil(sqrt)

    if lower % 2 == 0:
        lower = lower - 1

    if upper % 2 == 0:
        upper = upper + 1

    return [lower, upper]

def get_level(input):
    level = 0
    odd_counter = 1
    while int(input) > int(odd_counter * odd_counter):
        odd_counter = odd_counter + 2
        level = level + 1
    return level

def manhattan_distance(start, finish=[0,0]):
    return abs(finish[0] - start[0]) + abs(finish[1] - start[1])

def get_position(input):
    level = 0
    odd_counter = 1
    while int(input) > int(odd_counter * odd_counter):
        odd_counter = odd_counter + 2
        level = level + 1

    start = odd_counter * odd_counter
    end = (odd_counter + 1) * (odd_counter + 1)

    y = math.sin( (((input - start - 1)/(end - start)) * 2 * math.pi) )
    x = math.cos( (((input - start - 1)/(end - start)) * 2 * math.pi) )

    return [
    ]

# Part Two
"""
147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806

1 = 1               1   n = n-1
2 = 1 + 1           2   n = n-1 + n-2
4 = 2 + 1 + 1       3   n = n-1 + n-2 + n-3
5 = 4 + 1           4   n = n-1 + n-4
10 = 5 + 4 + 1      5   n = n-1 + n-2 + n-5
11 = 10 + 1         6   n = n-1 + n-6
23 = 11 + 10 + 1    7   n = n-1 + n-2 + n-7 + n-8
25 = 23 + 1 + 1     8   n = n-1 + n-7 + n-8
26 = 25 + 1         9   n = n-1 + n-8
54 = 26 + 25 + 1    10  n = n-1 + n-2 + n-8 + n-9
57 = 54 + 2 + 1     11  n = n-1 + n-9 + n-10
59 = 57 + 2         12  n = n-1 + n-10
122 = 59 + 5    7 + 2
133 = 122 + 4 + 2
142 = 133 + 5 + 4
147 = 142 + 5
304 = 304 + 10 + 5

"""

