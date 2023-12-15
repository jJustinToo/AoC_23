with open('./8_hauntedWasteland/input.txt', 'r') as file:
    input = file.readlines()

# THIS FILE WILL WORK IF YOU WAIT 2 HOURS 46 MINS 40 SECS

def main():
    
    movementCommands = input[0].strip("\n")
    
    codes = []
    values = []
    for i in range(2, len(input)):
        letD = input[i].strip("\n").split(" = ")
        codes.append(letD[0]) 
        values.append(letD[1].strip("()").split(", "))
    
    A_Codes = []
    for code in codes:
        if code[2] == "A":
            A_Codes.append(code)
    
    print(A_Codes)
    
    zeds = []
    steps = 0
    i = 0
    while len(zeds) < len(A_Codes):
        steps += 1
        if i == len(movementCommands):
            i = 0
        
        
        for j, code in enumerate(A_Codes):
            
            if movementCommands[i] == 'L':
                A_Codes[j] = values[codes.index(code)][0]
            elif movementCommands[i] == 'R':
                A_Codes[j] = values[codes.index(code)][1]

        zeds = []
        for code in A_Codes:
            if code[2] == "Z":
                zeds.append(code[2])
        i += 1
        
        print(A_Codes, steps)
        
    print(steps)
    
    return
    

main()