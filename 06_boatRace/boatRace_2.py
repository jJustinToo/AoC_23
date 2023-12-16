with open('./6_boatRace/input.txt', 'r') as file:
    input = file.readlines()

def main():
    
    # Holding down for 1 second. speed += 1. 
    
    times = input[0].split()[1:]
    records = input[1].split()[1:]
    
    newTime = ''
    for time in times:
        newTime += time
    newTime = int(newTime)
    
    newRecord = ''
    for record in records:
        newRecord += record
    newRecord = int(newRecord)
    
    count = 0
    for holdTime in range(newTime):
        distance = (newTime - holdTime) * holdTime
        if distance > newRecord:
            count += 1

    print(count)
    return


main()