sum = 0

with open('input.txt') as f:
    for line in f:
        digits = ''.join(x for x in line if x.isdigit())
        sum += int(digits[0] + digits[-1])
        print(str(int(digits[0] + digits[-1])))

print('answer = ' + str(sum))