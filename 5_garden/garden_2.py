with open('./5_garden/input.txt', 'r') as file:
    inputs = file.readlines()

def main():
    seed = list(map(int, inputs[0].strip("\n").split(" ")[1:]))

    seeds = []
    for i in range(0, len(seed), 2):
        seeds.append((seed[i], seed[i] + seed[i + 1]))

    for maps in findMaps():
        newSeeds = []
        while len(seeds) > 0:
            start, end = seeds.pop() # Get the start and end range of a seed. 
            for dstStart, srcStart, rangeLen in maps: # Iterates over every map. 
                overlap_s = max(start, srcStart) # Overlap start. 
                overlap_e = min(end, srcStart + rangeLen) # Overlap 
                if overlap_s < overlap_e: # If there is overlap
                    newSeeds.append((overlap_s - srcStart + dstStart, overlap_e - srcStart + dstStart))
                    if overlap_s > start: # If there are some values not in the overlap.
                        seeds.append((start, overlap_s))
                    if end > overlap_e: # If there is some values after the overlap/
                        seeds.append((overlap_e, end))
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