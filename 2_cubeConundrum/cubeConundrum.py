def main():
    with open("./2_cubeConundrum/input.txt", 'r') as file:
        input = file.readlines()
    
    redCubes = 12
    greenCubes = 13
    blueCubes = 14
    
    sum = 0
    for i in range(len(input)):
        red = []
        green = []
        blue = []
        id = i + 1
        newInput = input[i].removeprefix('Game ' + str(i + 1) +':').strip('\n').split(';')
        
        for j in range(len(newInput)):
            if newInput[j].find('red') >= 0:
                if newInput[j][newInput[j].find('red') - 3] != ' ':
                    red.append(int(newInput[j][newInput[j].find('red') - 3]) * 10 + int(newInput[j][newInput[j].find('red') - 2]))
                else: 
                    red.append(int(newInput[j][newInput[j].find('red') - 2]))
            if newInput[j].find('green') >= 0:
                if newInput[j][newInput[j].find('green') - 3] != ' ':
                    green.append(int(newInput[j][newInput[j].find('green') - 3]) * 10 + int(newInput[j][newInput[j].find('green') - 2]))
                else: 
                    green.append(int(newInput[j][newInput[j].find('green') - 2]))
            if newInput[j].find('blue') >= 0:
                if newInput[j][newInput[j].find('blue') - 3] != ' ':
                    blue.append(int(newInput[j][newInput[j].find('blue') - 3]) * 10 + int(newInput[j][newInput[j].find('blue') - 2]))
                else: 
                    blue.append(int(newInput[j][newInput[j].find('blue') - 2]))
        
        # print(f"{red} + {green} + {blue}")
        
        if max(red) <= redCubes and max(green) <= greenCubes and max(blue) <= blueCubes:
            sum += id
                    
    print(sum)
    return


main()