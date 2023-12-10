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
    
    # for i in range(len(input)):
    i = 0
    while i < len(input):
        if i in indexOfNums:
            posOfNum = indexOfNums.index(i) # 1
            numberValue = stringNums[posOfNum] # 2
            print(numberValue, end='') 
            
            i += 1
            
        else: 
            print(input[i], end='')
            i += 1

    
    print(output)
    
    return


main()