inputs, *blocks = open('5_garden/input.txt').read().split("\n\n")

inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []
for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

for block in blocks:
    # Iterate over every block
    maps = []
    for line in block.splitlines()[1:]:
        maps.append(list(map(int, line.split())))
    
    # print(maps[0])
    newSeeds = []
    while len(seeds) > 0:
        start, end = seeds.pop() # Get the start and end range of a seed. 
        for dstStart, srcStart, rangeLen in maps: # Iterates over every map. 
            os = max(start, srcStart) # Overlap start. 
            oe = min(end, srcStart + rangeLen) # Overlap 
            if os < oe: # If there is overlap
                newSeeds.append((os - srcStart + dstStart, oe - srcStart + dstStart))
                if os > start: # If there are some values not in the overlap.
                    seeds.append((start, os))
                if end > oe: # If there is some values after the overlap/
                    seeds.append((oe, end))
                break
        else:
            newSeeds.append((start, end))
    seeds = newSeeds
# print(sorted(seeds))
print(min(seeds)[0])