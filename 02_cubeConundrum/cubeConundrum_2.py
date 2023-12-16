def main():
    with open("./2_cubeConundrum/input.txt", 'r') as file:
        input = file.readlines()
    
    redCubes = 12
    greenCubes = 13
    blueCubes = 14
    
    sum = 0
    for i in range(len(input)):
        red, green, blue = [], [], []
        input[i] = input[i].removeprefix('Game ' + str(i + 1) +':').strip('\n').split(';')
        
        for j in range(len(input[i])):
            if input[i][j].find('red') >= 0:
                if input[i][j][input[i][j].find('red') - 3] != ' ':
                    red.append(int(input[i][j][input[i][j].find('red') - 3]) * 10 + int(input[i][j][input[i][j].find('red') - 2]))
                else: 
                    red.append(int(input[i][j][input[i][j].find('red') - 2]))
            if input[i][j].find('green') >= 0:
                if input[i][j][input[i][j].find('green') - 3] != ' ':
                    green.append(int(input[i][j][input[i][j].find('green') - 3]) * 10 + int(input[i][j][input[i][j].find('green') - 2]))
                else: 
                    green.append(int(input[i][j][input[i][j].find('green') - 2]))
            if input[i][j].find('blue') >= 0:
                if input[i][j][input[i][j].find('blue') - 3] != ' ':
                    blue.append(int(input[i][j][input[i][j].find('blue') - 3]) * 10 + int(input[i][j][input[i][j].find('blue') - 2]))
                else: 
                    blue.append(int(input[i][j][input[i][j].find('blue') - 2]))
        
        # print(f'{red} + {green} + {blue}')
        power = (max(red) * max(green) * max(blue))
        sum += power
                    
    print(sum)
    return


main()