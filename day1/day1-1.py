f = open("inputs1-1.txt", "r")
lines = f.readlines()
summ = 0
for line in lines:
    digits = [str(x) for x in list(line) if x.isdigit()]
    if (len(digits) > 0):
        summ += int(digits[0]+digits[len(digits) - 1])

print(summ)