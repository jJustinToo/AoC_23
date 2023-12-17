with open('./13_pointOfIncidence/input.txt', 'r') as file:
    input = file.read().split("\n\n")

def main():
    ans = 0
    for block in input:
        block = block.splitlines()
        horiLine = findHorizontalLine(block)
        if horiLine == None:
            newBlock = []
            for j, col in enumerate(block[0]):
                column = ""
                for i, row in enumerate(block):
                    column += block[i][j]
                newBlock.append(column)
            vertLine = findHorizontalLine(newBlock)
            print(vertLine, "Vertical")
            
            if len(vertLine) > 1:
                for line in vertLine:
                    ans += line[0]
            else:
                ans += vertLine[0][0]
        else:
            print(horiLine, "Horizontal")
            
            if len(horiLine) > 1:
                for line in horiLine:
                    ans += line[0] * 100
            else:
                ans += horiLine[0][0] * 100
        
    print(ans)
    return

def findHorizontalLine(block):
    prevRow = (0, 0)
    verticalLines = []
    for i, row in enumerate(block, 1):
        if row == prevRow[0]:
            verticalLines.append((prevRow[1], i))
        else:
            prevRow = (row, i)
    
    if verticalLines == []:
        return None
    
    validLines = []
    for verticalLine in verticalLines:
        if checkHoriLine(verticalLine, block) != None:
            validLines.append(verticalLine)    
        
    # print(validLines[0])
    if validLines == []:
        return None
    return validLines
        

def checkHoriLine(line, block):
    # Closest distance from the edge. 
    distancesFromStart = [abs(0 - line[0]), abs(0 - line[1])]
    distancesFromEnd = [abs(len(block) - line[0]), abs(len(block) - line[1])]
    closestDistance = min(min(distancesFromEnd), min(distancesFromStart))
    
    for i in range(closestDistance):
        if block[line[0] - 1 - i] != block[line[1] - 1 + i]:
            return None
    
    return line

main()