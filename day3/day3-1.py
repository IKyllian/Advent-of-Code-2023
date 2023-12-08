f = open("inputs3.txt", "r")
lines = f.readlines()
symbols = "0123456789."
summ = 0

def get_numbers_index(line):
    numberIndex = []
    number = ""
    ret = []
    for letterIdx, letter in enumerate(line):
        if letter.isdigit():
            numberIndex.append(letterIdx)
            number += letter
        else:
            if len(numberIndex) > 0:
                ret.append((numberIndex[0], numberIndex[len(numberIndex) - 1], int(number)))
                numberIndex.clear()
                number = ""
    return ret

def check_case(index, nb, line) :
    columnStart = index - 1 if index - 1 >= 0 else index
    columnEnd = index + 2 if index + 2 < len(lines) else len(lines) - 1
    rowStart = nb[0] - 1 if nb[0] - 1 >= 0 else nb[0]
    rowEnd = nb[1] + 2 if nb[1] + 2 < len(line) else len(line) - 1
    for x in range(columnStart, columnEnd):
        for y in range(rowStart, rowEnd):
            if lines[x][y] not in symbols:
                return True
    return False

index = 0
for lineIdx, line in enumerate(lines):
    numbers = get_numbers_index(line)
    for nb in numbers:
            if check_case(index, nb, line) == True:
                summ += nb[2]
    index += 1
print(summ)