def main():
    numbers = ('zero','one','two','three','four','five','six','seven','eight','nine')
    # input = "eightwothree"
    input = "xtwone3four"
    # Output should equal '823'
    
    # list2 = [2, 3, 8] Numbers in the string
    # list = [4, 7, 0] Index at which the corresponding numbers can be found. 
    stringNums = []
    indexOfNums = []
    
    for k in range(len(numbers)):
        index = input.find(numbers[k])
        if index >= 0:
            stringNums.append(k)
            indexOfNums.append(index)
    
    print(stringNums)
    print(indexOfNums)
    
    output = ''
    
    for i in range(len(input)):
        if i in indexOfNums:
            posOfNum = indexOfNums.index(i) # 1
            numberValue = stringNums[posOfNum] # 2
            print(numberValue, end='') 
            
            
            # Skip to two len away
            # if i > 
            
            # newPos should be i + len(blah) 
            # But if newPos is greater than or equal to another item in index besides 'i'
            # Set i = the value that it is greater than or equal to. 
            # 
            
        else: 
            print(input[i], end='')

    
    print(output)
    
    return


main()