sum = 0
str_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# thanks to u/whatyoucallmetoday - I was close but needed this small adjustment to get it to work
# https://github.com/colonwq/aoc/blob/master/2023/day01/code-3.py#L34-L48
replacements = {
"zerone": "zeroone",
"oneight": "oneeight",
"twone": "twoone",
"sevenine": "sevennine",
"eightwo": "eighttwo",
"eighthree": "eightthree",
"nineight": "nineeight"
}


with open('input.txt') as f:
    for line in f:
        print(line)
        
        for replacement in replacements.keys():
            line = line.replace(replacement, replacements[replacement])

        for dig in range(0, len(str_digits)):
            if str_digits[dig] in line:
                line = line.replace(str_digits[dig], str(dig+1))
        print(line)

        digits = ''.join(x for x in line if x.isdigit())
        sum += int(digits[0] + digits[-1])
        print(str(int(digits[0] + digits[-1])))

print('answer = ' + str(sum))