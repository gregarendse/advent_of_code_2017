def captcha(input):
    count = 0
    for i in range(len(input)):
             if input[i] == input[(i+1) % len(input)]:
                     count = count + int(input[i])
    return count

def part_two(input):
    count = 0
    input_len = int(len(input))
    for i in range(input_len):
        if input[i] == input[int((i + (input_len / 2)) % input_len)]:
            count = count + int(input[i])
    return count

def read(file_path):
    with open(file_path) as file:
        input = file.read()
    return input
