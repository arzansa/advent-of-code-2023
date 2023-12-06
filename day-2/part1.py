max_red = 12
max_green = 13
max_blue = 14
sum = 0

with open('input.txt') as f:

    for line in f:

        possible = True

        cubes = (''.join(i for i in line if i.isdigit() or
                       i in ' ')).split()
        colors = (''.join(i for i in line if i.isalpha() or
                       i in ' ')).split()
        
        gamenum = cubes.pop(0)
        colors.pop(0)


        #nal = noalpha.split()
        #al = alpha.split() 

        #game_num = noalpha[0]
        
        for i in range(0, len(cubes)):
                
            if colors[i] == 'red':
                if int(cubes[i]) > max_red:
                    possible = False

            elif colors[i] == 'green':
                if int(cubes[i]) > max_green:
                    possible = False

            elif colors[i] == 'blue':
                if int(cubes[i]) > max_blue:
                    possible = False
        
        if (possible):
            print(f'Game {gamenum} is possible')
            sum += int(gamenum)
        else:
            print(f'Game {gamenum} is impossible')

print(f'Solution is {sum}')