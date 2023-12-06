max_red = 12
max_green = 13
max_blue = 14
possible = False

with open('input.txt') as f:
    for line in f:
        nums = line.join(i for i in line if i.isdigit())
        print(nums)