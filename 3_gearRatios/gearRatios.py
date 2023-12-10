def main():
    with open("./3_gearRatios/example.txt", 'r') as file:
        input = file.readlines()
    
    symbols = '!@#$%^?><,/&*+_=-'
        
    for i in range(len(input)):
        # input[i] = input[i].strip('\n')
        for j in range(len(input[i])):
            # print(input[i][j], end='')
            if input[i][j] in symbols:
                print(input[i-1][j-1] + input[i-1][j] + input[i-1][j+1])
                print(input[i][j-1] + input[i][j] + input[i][j+1])
                print(input[i+1][j-1] + input[i+1][j] + input[i+1][j+1])
                print('STOP')
            
    return

main()