with open('./11_cosmicExpansion/example.txt', 'r') as file:
    input = file.readlines()

def main():
    # Finds empty columns indexes
    emptyCols = []
    for j, col in enumerate(input[0]):
        column = ""
        for i, row in enumerate(input):
            column += input[i][j]
        
        if all(x == "." for x in column):
            emptyCols.append(j)

    # Makes newInput
    newInput = []
    for i, line in enumerate(input):
        text = ""
        for j, char in enumerate(input[i]):
            if j in emptyCols:
                text += char
                text += char
            else:
                text += char
        text = text.strip("\n")
        
        if all(x == "." for x in line.strip("\n")):
            newInput.append(text)
            newInput.append(text)
        else:
            newInput.append(text)
    
    # Finds coords of all "#"
    
    coords = []
    for i, line in enumerate(newInput):
        for j, char in enumerate(newInput[i]):
            if newInput[i][j] == "#":
                coords.append((i, j))
    
    # Finds distances between all unique coords
    ans = 0
    for i, coord in enumerate(coords):
        for j in range(i, len(coords)):
            ans += (dist(coord, coords[j]))
        
    print(ans)
    return

def dist(a, b):
    i1, j1,  = a
    i2, j2 = b

    i1, i2 = min(i1, i2), max(i1, i2)
    j1, j2 = min(j1, j2), max(j1, j2)

    ans = 0
    for i in range(i1, i2):
        ans += 1
    for j in range(j1, j2):
        ans += 1

    return ans


main()