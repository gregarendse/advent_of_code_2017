import math

def get_bounds(input: int) -> [int, int]:
    upper = math.ceil(math.sqrt(int(input)))

    if upper % 2 == 0:
        upper = upper + 1

    lower = math.floor(math.sqrt(int(input)))

    if lower % 2 == 0:
        lower = lower - 1

    return [upper, lower]

def manhattan_distance(start: [int, int], finish: [int, int]) -> float:
    return abs(start[0] - finish[0]) + abs(start[1] + finish[1])

def get_level(input: int):
    odd_count = 1
    counter = 0
    while odd_count < input:
        odd_count = odd_count + 2
        counter = counter + 1

    return counter

def spiral_memory(input: int) -> float:
    [upper, lower] = get_bounds(input)
    r = get_level(lower) + 1
    print("r: ", r)
    count = (upper * upper) - (lower * lower)
    print("Count: ", count)
    deg_per_point = (2 * math.pi) / count
    print("Degrees per point: ", deg_per_point * (180/math.pi))
    pos = int(input) - (lower * lower)
    off_set = (math.pi / 4)
    print("Off set", off_set * (180/math.pi))

    print(((pos * deg_per_point)) * (math.pi/180))
    co_ord = [
        r * math.cos(((pos - r) * deg_per_point)),
        r * math.sin(((pos - r) * deg_per_point))
    ]

    print(co_ord)

    return manhattan_distance(start=co_ord, finish=[0,0])

# print("1: ", spiral_memory(1))
print("2: ", spiral_memory(2))
print("11: ", spiral_memory(11))
print("12: ", spiral_memory(12))
print("23: ", spiral_memory(23))
print("1024: ", spiral_memory(1024))