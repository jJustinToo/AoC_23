with open("./3_gearRatios/input.txt", 'r') as file:
    input = file.readlines()
    
def main():
    ans = 0
    symPositions = []
    numPositions = []
    for i in range(len(input)):
        j = 0
        while j < len(input[0]):
            
            symbolPos = []
            
            # Get Number
            start = j
            num = ''
            while j < len(input[0]) and input[i][j].isdigit():
                num += input[i][j]
                j += 1
            
            if num == '':
                j += 1
                continue
            
            num = int(num)
            
            # Finds Symbol Postion
            if isSymbol(i, start - 1) and isValidGear(i, start - 1):
                symbolPos.append(i)
                symbolPos.append(start - 1)
            
            if isSymbol(i, j) and isValidGear(i, j):
                symbolPos.append(i)
                symbolPos.append(j)
            
            for k in range(start - 1, j + 1):
                if isSymbol(i - 1, k) and isValidGear(i - 1, k):
                    symbolPos.append(i - 1)
                    symbolPos.append(k)
                    break
                if isSymbol(i + 1, k) and isValidGear(i + 1, k):
                    symbolPos.append(i + 1)
                    symbolPos.append(k)
                    break
            
            # If symbol has been found before, do the math. 
            # Else add it to the database
            if symbolPos in symPositions:
                ans += numPositions[symPositions.index(symbolPos)] * num
                numPositions.remove(numPositions[symPositions.index(symbolPos)])
                symPositions.remove(symbolPos)
            elif symbolPos != []:
                symPositions.append(symbolPos)
                numPositions.append(num)
            
    print(ans)
    
    return

def isSymbol(row, col):
    # symbols = '!@#$%^?><,/&*+_=-'
    symbols = '*'
    if isValidPos(row, col) == False:
        return False
    
    if input[row][col] in symbols:
        return True
    else: 
        return False
def isValidGear(row, col):
    nums = []
    for i in range(row - 1, row + 2):
        for j in range (col - 1, col + 2):
            if isValidPos(i, j) == False:
                return False
            if input[i][j].isdigit():
                nums.append(input[i][j])
    
    if len(nums) >= 2:
        return True
    else:
        return False
def isValidPos(row, col):
    if not (0 <= row < len(input) and 0 <= col < len(input[0])):
        return False
    else: 
        return True

main()