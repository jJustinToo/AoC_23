with open('./5_garden/example.txt', 'r') as file:
    input = file.readlines()

def main():
    seeds = input[0].removeprefix("seeds: ").strip().split(' ')
    
    seeds = list(map(int, seeds))
    
    newSeeds = []
    for i in range(0, len(seeds), 2):
        for j in range(seeds[i], seeds[i] + seeds[i+1]):
            newSeeds.append(j) 
    
    seeds = newSeeds
    print(seeds)
    
    seedPos = (input.index("seed-to-soil map:\n")) + 1
    soilPos = (input.index("soil-to-fertilizer map:\n")) + 1
    fertilizerPos = (input.index("fertilizer-to-water map:\n")) + 1
    waterPos = (input.index("water-to-light map:\n")) + 1
    lightPos = (input.index("light-to-temperature map:\n")) + 1
    temperaturePos = (input.index("temperature-to-humidity map:\n")) + 1
    humidityPos = (input.index("humidity-to-location map:\n")) + 1
    locationPos = len(input) - 1 + 2
    
    soils = newVersion(seeds, seedPos, soilPos)
    print(soils)
    fertilizers = newVersion(soils, soilPos, fertilizerPos)
    print(fertilizers)
    waters = newVersion(fertilizers, fertilizerPos, waterPos)
    print(waters)
    lights = newVersion(waters, waterPos, lightPos)
    print(lights)
    temperatures = newVersion(lights, lightPos, temperaturePos)
    print(temperatures)
    humidities = newVersion(temperatures, temperaturePos, humidityPos)
    print(humidities)
    location = newVersion(humidities, humidityPos, locationPos)
    print(location)
    
    return

def newVersion(list, start, end):
    newList = []
    for x in list:
        newList.append(mapper(x, checkMap(x, getMap(start, end))))
    return newList

def getMap(start, end):
    list = []
    for i in range(start, end - 2):
        list.append(input[i].strip("\n").split(" "))
    return list

def checkMap(input, maps):
    input = int(input)
    for mapi in maps: 
        if int(mapi[1]) <= input < int(mapi[1]) + int(mapi[2]):
            return mapi

def mapper(input, info):
    if info == None:
        return int(input)
    if int(info[1]) <= int(input) < int(info[1]) + int(info[2]):
        return (int(input) - int(info[1]) + int(info[0]))

main()