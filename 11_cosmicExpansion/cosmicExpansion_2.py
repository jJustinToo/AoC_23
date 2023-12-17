with open('./11_cosmicExpansion/input.txt', 'r') as file:
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

    # Finds empty rows indexes
    emptyRows = []
    for i, row in enumerate(input):
        if all(x == "." for x in row.strip("\n")):
            emptyRows.append(i)
    
    # Finds coords of all "#"
    coords = []
    for i, line in enumerate(input):
        for j, char in enumerate(input[i]):
            if input[i][j] == "#":
                coords.append((i, j))
    
    # Finds distances between all unique coords
    ans = 0
    for i, coord in enumerate(coords):
        for j in range(i, len(coords)):
            ans += (dist(coord, coords[j], emptyCols, emptyRows))
        
    print(ans)
    return

def dist(a, b, emptyCols, emptyRows):
    i1, j1 = a
    i2, j2 = b

    i1, i2 = min(i1, i2), max(i1, i2)
    j1, j2 = min(j1, j2), max(j1, j2)

    ans = 0
    for i in range(i1, i2):
        ans += 1
        if i in emptyRows:
            ans += 1000000 - 1
    for j in range(j1, j2):
        ans += 1
        if j in emptyCols:
            ans += 1000000 - 1

    return ans


main()