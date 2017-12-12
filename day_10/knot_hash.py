
def knot_hash_round(input, lengths, current_position=0, skip_size=0):
    for length in lengths:
        # print('lenght: ', length)
        end_position = (current_position + length)
        # print('current_position: ', current_position % len(input), 'end_position: ', end_position % len(input))
        if end_position % len(input) > current_position % len(input):
            original_list = input[current_position % len(input):end_position % len(input)]
        else:
            original_list = input[current_position % len(input):] + input[:end_position % len(input)]
        # print('original_list: ', original_list)

        for i in range(length):
            working_position = (current_position + i) % len(input)
            # print('working_position: ', working_position)
            extract_position = (len(original_list) - i - 1) % len(original_list)
            # print('extract_position: ', extract_position)
            input[working_position] = original_list[extract_position % len(original_list)]

        current_position = (current_position + length + skip_size)
        skip_size = skip_size + 1
    return [input, current_position, skip_size]

def knot_hash(input):
    ascii_codes = [ord(i) for i in str(input)]
    ascii_codes = ascii_codes + [17, 31, 73, 47, 23]
    position = 0
    size = 0
    for i in range(64):
        ranges = [int(i) for i in range(256)]
        [ascii_codes, position, size] = knot_hash_round(ranges, ascii_codes, position, size)

    print('sparse_hash: ', ascii_codes)
    dense = dense_hash(ascii_codes)
    print(dense)

    hex_str = to_hex(dense)
    print(hex_str)
    return hex_str

def to_hex(input):
    hex_str = ""
    for i in [hex(i) for i in input]:
        if len(i[2:]) == 2:
            hex_str = hex_str + i[2:]
        else:
            hex_str = hex_str + "0" + i[2:]
    return hex_str

assert to_hex([64, 7, 255]) == '4007ff'

def dense_hash(input):
    dense_hash = []
    for i in range(int(len(input) / 16)):
        dense_hash.append(0)
        for j in range(16):
            dense_hash[i] = dense_hash[i] ^ input[(i * 16) + j]
    return dense_hash

print(dense_hash([65 , 27 , 9 , 1 , 4 , 3 , 40 , 50 , 91 , 7 , 6 , 0 , 2 , 5 , 68 , 22]))
assert dense_hash([65 , 27 , 9 , 1 , 4 , 3 , 40 , 50 , 91 , 7 , 6 , 0 , 2 , 5 , 68 , 22]) == [64]

input = [int(i) for i in range(5)]
result = knot_hash_round(input, [3,4,1,5])
assert result[0][0] * result[0][1] == 12

ranges = [int(i) for i in range(5)]
print(knot_hash_round(ranges, [3, 4, 1, 5]))
# exit(0)

assert knot_hash("") == "a2582a3a0e66e6e86e3812dcb672a272"
# assert knot_hash("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
# assert knot_hash("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
# assert knot_hash("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"

# exit(0)

exit(0)

with open('day_10/input') as file:
    lengths = [int(i) for i in file.read().split(',')]

input = [int(i) for i in range(256)]
result = knot_hash(input, lengths)
print(result)
print(result[0] * result[1])
