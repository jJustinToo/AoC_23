with open('./10_pipeMaze/input.txt', 'r') as file:
    input = file.readlines()

def main():
    for row in range(len(input)):
        input[row] = input[row].strip("\n")
        col = input[row].find("S")
        if col >= 0:
            break
    
    ups, downs, lefts, rights = "7F|", "JL|", "FL-", "J7-"
    scan = []
    scan.append((row - 1, col) if isValidPos((row - 1, col)) and input[row - 1][col] in ups else None) # UP
    scan.append((row + 1, col) if isValidPos((row + 1, col)) and input[row + 1][col] in downs else None) # DOWN
    scan.append((row, col - 1) if isValidPos((row, col - 1)) and input[row][col - 1] in lefts else None) # LEFT 
    scan.append((row, col + 1) if isValidPos((row, col + 1)) and input[row][col + 1] in rights else None) # RIGHT
    while None in scan:
        scan.remove(None)
    
    visited = []
    previousCoord = (row, col)
    sPos = (row, col)
    curCoord = scan[0]
    row, col = curCoord
    visited.append(sPos)
    visited.append(curCoord)
    
    steps = 0
    while input[row][col] != "S":
        possibleCoords = []
        row, col = curCoord
        up, down, left, right = (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)
        letter = input[row][col]
        
        if curCoord == sPos:
            break
        
        if letter == "|":
            if isValidPos(down):
                possibleCoords.append(down)
            if isValidPos(up):
                possibleCoords.append(up)
        elif letter == "-":
            if isValidPos(left):
                possibleCoords.append(left)
            if isValidPos(right):
                possibleCoords.append(right) 
        elif letter == "L":
            if isValidPos(up):
                possibleCoords.append(up)
            if isValidPos(right):
                possibleCoords.append(right)
        elif letter == "J":
            if isValidPos(left):
                possibleCoords.append(left)
            if isValidPos(up):
                possibleCoords.append(up)
        elif letter == "7":
            if isValidPos(down):
                possibleCoords.append(down)
            if isValidPos(left):
                possibleCoords.append(left)
        elif letter == "F":
            if isValidPos(down):
                possibleCoords.append(down)
            if isValidPos(right):
                possibleCoords.append(right)
            
        possibleCoords.remove(previousCoord)
        previousCoord = curCoord
        curCoord = possibleCoords[0]
        visited.append(possibleCoords[0])
        steps += 1
    
    ans = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if (checkIntersections(i, j, visited)) and (i, j) not in visited:
                ans += 1
    
    print(ans)
    return

def checkIntersections(row, col, visited):
    
    line = input[row].strip("\n")
    intersections = 0
    for i in range(col, len(input[row])):
        if (row, i) in visited:
            if input[row][i] == "|" or input[row][i] == "J" or input[row][i] == "L": 
                intersections += 1
    
    if intersections % 2 == 1:
        return True # The point is in the loop
    else:
        return False
        

def isValidPos(x):
    row = x[0]
    col = x[1]
    
    if (0 <= row < len(input) and 0 <= col < len(input[0])):
        return True

main()