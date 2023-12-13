with open('./5_garden/example.txt', 'r') as file:
    input = file.readlines()

def main():
    seeds = list(map(int, input[0].strip("\n").split(" ")[1:]))
    
    maps = findMaps()
    
    seedRanges = []
    for s in range(0, len(seeds), 2):
        seedRanges.append((seeds[s], seeds[s] + seeds[s+1]))

    print(seedRanges)
    
    # (1, 100)
    # (1, 50) (50, 98) (98, 100)    

def findMaps():
    maps = []
    i = 2
    while i < len(input):
        mapss = []
        
        i += 1
        while i < len(input) and not input[i] == "\n":
            dstStart, srcStart, rangeLen = map(int, input[i].strip('\n').split())
            mapss.append((dstStart, srcStart, rangeLen))
            i += 1
        
        maps.append(mapss)    
        i += 1
        
    return maps
        
def findLocation(input, maps):
    num = input
    for map in maps:
        for dstStart, srcStart, rangeLen in map:
            if srcStart <= num < srcStart + rangeLen:
                num = num - srcStart + dstStart
                break
                
    return num


main()