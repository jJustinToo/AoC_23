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
        
        stringNums = []
        indexOfNums = []
        
        for k in range(len(numbers)):
            index = input[i].find(numbers[k])
            if index >= 0:
                stringNums.append(k)
                indexOfNums.append(index)
        
        # print(stringNums)
        # print(indexOfNums)
        
        output = ''
        
        for j in range(len(input[i])):
            if j in indexOfNums:
                posOfNum = indexOfNums.index(j) # 1
                numberValue = stringNums[posOfNum] # 2
                # print(numberValue, end='') 
                output += str(numberValue)
                
                # Skip to two len away
                # if i > 
                
                # newPos should be i + len(blah) 
                # But if newPos is greater than or equal to another item in index besides 'i'
                # Set i = the value that it is greater than or equal to. 
                # 
                
            else: 
                # print(input[i][j], end='')
                output += str(input[i][j])

        
        print(output)
        input[i] = output
        # Changed Sentence
        # print(input[i])
        a = 0
        b = 0
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