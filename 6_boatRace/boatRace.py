with open('./6_boatRace/example.txt', 'r') as file:
    input = file.readlines()

def main():
    
    # Holding down for 1 second. speed += 1. 
    
    times = list(map(int, input[0].split()[1:]))
    records = list(map(int, input[1].split()[1:]))
    
    ans = 1
    for i, time in enumerate(times):
        count = 0
        for holdTime in range(time):
            distance = (time - holdTime) * holdTime
            if distance > records[i]:
                count += 1

        ans = ans * count
        
        
    print(ans)
    return


main()