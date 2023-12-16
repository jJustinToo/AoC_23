with open('./5_garden/input.txt', 'r') as file:
    inputs = file.readlines()

def main():
    seed = list(map(int, inputs[0].strip("\n").split(" ")[1:]))

    seeds = []
    seeds.extend([(seed[i], seed[i] + seed[i + 1]) for i in range(0, len(seed), 2)])       

    for maps in findMaps():
        newSeeds = []
        for start, end in seeds:
            for dstStart, srcStart, rangeLen in maps: # Iterates over every map. 
                matchRange_s = max(start, srcStart) # Overlap start. 
                matchRange_e = min(end, srcStart + rangeLen) # Overlap 
                if matchRange_s < matchRange_e: # If there is overlap
                    newSeeds.append((matchRange_s - srcStart + dstStart, matchRange_e - srcStart + dstStart))
                    if matchRange_s > start: # If there are some values not in the overlap.
                        seeds.append((start, matchRange_s))
                    if end > matchRange_e: # If there is some values after the overlap/
                        seeds.append((matchRange_e, end))
                    break
            else:
                newSeeds.append((start, end))
        seeds = newSeeds
        
    
    print(min(seeds)[0])
    

def findMaps():
    maps = []
    i = 2
    while i < len(inputs):
        mapss = []
        
        i += 1
        while i < len(inputs) and not inputs[i] == "\n":
            dstStart, srcStart, rangeLen = map(int, inputs[i].strip('\n').split())
            list = [dstStart, srcStart, rangeLen]
            mapss.append(list)
            i += 1
        
        maps.append(mapss)    
        i += 1
        
    return maps


main()