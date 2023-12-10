def main():
    # 1abc2 = 12
    # pqr3stu8vwx = 38
    # a1b2c3d4e5f = 15
    # treb7uchet = 77
    
    with open("./1_trebuchet/input.txt", 'r') as file:
        input = file.readlines()
        
    sum = 0
    numbers = ('zero','one','two','three','four','five','six','seven','eight','nine')
    
    # Search Every Line
    for i in range(len(input)):
        input[i] = input[i].strip("\n")
        
        for k in range(len(numbers)):
            index = input[i].find(numbers[k])
            if index >= 0:
                # input[i] = input[i].replace(numbers[k], str(k))
                input[i] = input[i][:index] + str(k) + input[i][index:]

        for num in numbers:
            input[i] = input[i].replace(num, '')
        
        print(input[i])
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