import math

with open('./8_hauntedWasteland/input.txt', 'r') as file:
    input = file.readlines()

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
    
    stepList = []
    for curCode in A_Codes:
        steps = 0
        i = 0
        while curCode[2] != "Z":
            if i == len(movementCommands):
                i = 0
            if movementCommands[i] == 'L':
                curCode = values[codes.index(curCode)][0]
            elif movementCommands[i] == 'R':
                curCode = values[codes.index(curCode)][1]
            steps += 1
            i += 1
        stepList.append(steps)
    
    print(math.lcm(*stepList))
    return
    

main()