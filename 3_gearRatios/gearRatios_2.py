with open("./3_gearRatios/input.txt", 'r') as file:
    input = file.readlines()
    
def main():
    ans = 0
    Sym_Nums = {}
    for i in range(len(input)):
        # Iterate over every char
        j = 0
        while j < len(input[0]):
            start = j
            num = ''
            while j < len(input[0]) and input[i][j].isdigit():
                num += input[i][j]
                j += 1
            if num == '':
                j += 1
                continue
            
            num = int(num)
            symbolPos = findSymbolPos(i,j,start)
            
            if str(symbolPos) in Sym_Nums:
                ans += Sym_Nums[str(symbolPos)] * num
                Sym_Nums.pop(str(symbolPos))
            elif symbolPos != []:
                Sym_Nums[str(symbolPos)] = num
            
    print(ans)
    
    return

def findSymbolPos(i, j, start):
    symbolPos = []
    if isValidGear(i, start - 1):
        symbolPos.append(i)
        symbolPos.append(start - 1)
    
    elif isValidGear(i, j):
        symbolPos.append(i)
        symbolPos.append(j)
    
    for k in range(start - 1, j + 1):
        if isValidGear(i - 1, k):
            symbolPos.append(i - 1)
            symbolPos.append(k)
            break
        elif isValidGear(i + 1, k):
            symbolPos.append(i + 1)
            symbolPos.append(k)
            break
    
    return symbolPos
   
def isValidGear(row, col):
    nums = []
    symbols = '*'
    
    if (0 <= row < len(input) and 0 <= col < len(input[0])) and input[row][col] in symbols:
        for i in range(row - 1, row + 2):
            for j in range (col - 1, col + 2):
                if (0 <= row < len(input) and 0 <= col < len(input[0])) and input[i][j].isdigit():
                    nums.append(input[i][j])
        
        if len(nums) >= 2:
            return True
        else:
            return False
    else: 
        return False
    

main()