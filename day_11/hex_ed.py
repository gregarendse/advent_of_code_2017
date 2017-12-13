
def distance(input) -> int:
    instruction_map = {}
    x = 0
    y = 0
    x = 0
    distance = 0
    previous_move = None
    for move in input:
        if 'n' == move:
            y = y + 1
        elif 'ne' == move:
            z = z + 1
        elif 'se' == sub_move:
        elif 's' == sub_move:
        elif 'sw' == sub_move:
        elif 'nw' == move:
        else:
            raise Exception('Unknown sub-move: ', sub_move)

    print("x: {x}, y: {y}".format(x=x, y=y))
    difference = abs(abs(x) - abs(y))
    same = abs(min(x, y))
    result = same + difference
    # result = (abs(0 - x) + abs(0 - y))/2
    print(result)
    return result

assert distance(['ne','ne','ne']) == 3
assert distance(['ne','ne','sw', 'sw']) == 0
assert distance(['ne','ne','s', 's']) == 2
assert distance(['se','sw','se', 'sw', 'sw']) == 3
