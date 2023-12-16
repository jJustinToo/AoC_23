with open('./9_sequencePredictions/input.txt', 'r') as file:
    input = file.readlines()

def main():
    
    ans = 0
    
    for line in input:
        values = list(map(int, line.strip("\n").split()))
        # values.reverse() # ADD THIS LINE FOR PART TWO 
        diffs = getDiffs(values)
        
        values.append(values[-1] + diffs[-1])
        ans += (values[-1])
        # print(values[-1])
        
    print(ans)
    return

def getDiffs(list):
    diffs = []
    for i, item in enumerate(list):
        if i != len(list) - 1:
            diffs.append((item - list[i+1]) * -1)

    if all(i == 0 for i in diffs) == False:
        diffs.append(getDiffs(diffs)[-1] + diffs[-1])
        return diffs
    else: 
        diffs.append(0)
        return diffs
        



main()