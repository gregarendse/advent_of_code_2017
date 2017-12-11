def checksum(input):
    checksum = 0
    for row in input:
        max = None
        min = None
        for column in row:
            if max == None or max < int(column):
                max = int(column)
            if (min == None) or (min > int(column)):
                min = int(column)

        checksum = checksum + (max - min)
    return checksum

def even_divide(input):
    checksum = 0
    for row in input:
        for i in range(len(row)):
            for j in range(len(row)):
                if row[i] == row[j]:
                    continue

                div = int(row[i]) / int(row[j])
                even_div = int(div)

                if div == even_div:
                    checksum = checksum + (even_div)
                    break
    return checksum

def parseInput(input):
    with open(input) as file:
        content = file.read()

    lines = content.split('\n')

    output = []
    for line in lines:
        new = []
        for item in line.split():
            new.append(item)
        output.append(new)

    return output

