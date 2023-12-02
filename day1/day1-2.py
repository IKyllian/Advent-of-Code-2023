numbers = {
    ("one", '1'),
    ("two", '2'),
    ("three", '3'),
    ("four", '4'),
    ("five", '5'),
    ("six", '6'),
    ("seven", '7'),
    ("eight", '8'),
    ("nine", '9'),
}
def search_numbers(lst, s):
    ret = []
    for number in lst:
        start = 0
        while not s.find(number[0], start) == -1:
            ret.append((number[1], s.index(number[0], start)))
            start = s.index(number[0], start) + len(number[0])
    return ret

f = open("inputs1-1.txt", "r")
lines = f.readlines()
summ = 0
for line in lines:
    # Take all digits
    digits = [(str(x), idx) for idx, x in enumerate(list(line)) if x.isdigit()]
    # Add all string digits (outputs converted to digit)
    digits = digits + search_numbers(numbers, line)
    # Sort by index order
    digits = sorted(digits, key=lambda d: d[1])
    
    if (len(digits) > 0):
        summ += int(digits[0][0]+digits[len(digits) - 1][0])

print(summ)
