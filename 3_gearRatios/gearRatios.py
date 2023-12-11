with open("./3_gearRatios/input.txt", 'r') as file:
    input = file.readlines()
    
def main():
    ans = 0
    for i in range(len(input)):
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
            
            if isSymbol(i, start - 1) or isSymbol(i, j):
                ans += num
                continue
            
            for k in range(start-1, j + 1):
                if isSymbol(i-1, k) or isSymbol(i+1, k):
                    ans += num
                    break
            
    print(ans)
    return

def isSymbol(row, col):
    symbols = '!@#$%^?><,/&*+_=-'
    
    if not (0 <= row < len(input) and 0 <= col < len(input[0])):
        return False
    
    if input[row][col] in symbols:
        return True
    else: 
        return False


main()