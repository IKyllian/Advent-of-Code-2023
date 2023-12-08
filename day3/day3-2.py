f = open("inputs3.txt", "r")
lines = f.readlines()
symbols = "0123456789."
summ = 0

def get_numbers_index(line, lineIdx):
    numberIndex = []
    number = ""
    ret = []
    for letterIdx, letter in enumerate(line):
        if letter.isdigit():
            numberIndex.append(letterIdx)
            number += letter
        else:
            if len(numberIndex) > 0:
                ret.append((lineIdx, numberIndex[0], numberIndex[len(numberIndex) - 1], int(number)))
                numberIndex.clear()
                number = ""
    return ret

def get_symbols(line):
    symbols = []
    for letterIdx, letter in enumerate(line):
        if letter == '*':
            symbols.append((letterIdx))
    return symbols

def find_number(columnIndex, rowIndex):
    numbers = get_numbers_index(lines[columnIndex], columnIndex)
    for nb in numbers:
        if nb[0] == columnIndex and \
        (nb[1] == rowIndex or nb[1] - 1 == rowIndex or nb[1] + 1 == rowIndex or \
        nb[2] == rowIndex or nb[2] - 1 == rowIndex or nb[2] + 1 == rowIndex):
            return nb[3]
    return False

def check_case(index, symbol, line) :
    columnStart = index - 1 if index - 1 >= 0 else index
    columnEnd = index + 2 if index + 2 < len(lines) else len(lines)
    rowStart = symbol - 1 if symbol - 1 >= 0 else symbol
    rowEnd = symbol + 2 if symbol + 2 < len(line) else len(line)
    numbersFound = []
    count = 0
    ret = 1
    for x in range(columnStart, columnEnd):
        for y in range(rowStart, rowEnd):
            if lines[x][y].isdigit():
                found = find_number(x, y)
                if found and found not in numbersFound:
                    count += 1
                    numbersFound.append(found)
                    ret *= found
                    if count == 2:
                        break
        if count == 2:
            break
    return ret if count == 2 else False

index = 0
for lineIdx, line in enumerate(lines):
    symbols = get_symbols(line)
    for symbol in symbols:
        ret = check_case(index, symbol, line)
        if not ret == False:
            summ += ret
    index += 1
print(summ)