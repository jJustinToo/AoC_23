def main():
    
    with open("./1_trebuchet/input.txt", 'r') as file:
        input = file.readlines()
        
    sum = 0
    numbers = ('zero','one','two','three','four','five','six','seven','eight','nine')

    for i in range(len(input)):
        input[i] = input[i].strip("\n")
        for k in range(len(numbers)):
            index = input[i].find(numbers[k])
            if index >= 0:
                input[i] = input[i].replace(numbers[k], numbers[k] + str(k) + numbers[k])
        
        a = 0
        for letter in input[i]:
            if letter.isnumeric() and a == 0:
                a = int(letter)
                b = int(letter)
            elif letter.isnumeric(): 
                b = int(letter)
        
        sum += (a * 10) + b 
    
    print(sum)    
    return


main()