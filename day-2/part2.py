max_red = 12
max_green = 13
max_blue = 14
sum = 0
sum_of_powers = 0

with open('input.txt') as f:

    for line in f:

        possible = True
        min_red = 0
        min_green = 0
        min_blue = 0
        power_of_mins = 0

        cubes = (''.join(i for i in line if i.isdigit() or
                       i in ' ')).split()
        colors = (''.join(i for i in line if i.isalpha() or
                       i in ' ')).split()
        
        gamenum = cubes.pop(0)
        colors.pop(0)
        
        for i in range(0, len(cubes)):

            if colors[i] == 'red':
                if int(cubes[i]) > max_red:
                    possible = False
                if int(cubes[i]) > min_red:
                    min_red = int(cubes[i])

            elif colors[i] == 'green':
                if int(cubes[i]) > max_green:
                    possible = False
                if int(cubes[i]) > min_green:
                    min_green = int(cubes[i])

            elif colors[i] == 'blue':
                if int(cubes[i]) > max_blue:
                    possible = False
                if int(cubes[i]) > min_blue:
                    min_blue = int(cubes[i])
        
        if (possible):
            #print(f'Game {gamenum} is possible')
            sum += int(gamenum)
        #else:
            #print(f'Game {gamenum} is impossible')
        power_of_mins = min_red * min_green * min_blue
        sum_of_powers += power_of_mins

print(f'Part 1 solution is {sum}')
print(f'Part 2 solution is {sum_of_powers}')