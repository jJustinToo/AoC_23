with open('./5_garden/example.txt', 'r') as file:
    input = file.readlines()

def main():
    seeds = input[0].removeprefix("seeds: ").strip().split(' ')
    
    seedPos = (input.index("seed-to-soil map:\n")) + 1
    soilPos = (input.index("soil-to-fertilizer map:\n")) + 1
    fertilizerPos = (input.index("fertilizer-to-water map:\n")) + 1
    waterPos = (input.index("water-to-light map:\n")) + 1
    lightPos = (input.index("light-to-temperature map:\n")) + 1
    temperaturePos = (input.index("temperature-to-humidity map:\n")) + 1
    humidityPos = (input.index("humidity-to-location map:\n")) + 1
    locationPos = len(input) - 1 + 2
    
    soils = newVersion(seeds, seedPos, soilPos)
    fertilizers = newVersion(soils, soilPos, fertilizerPos)
    waters = newVersion(fertilizers, fertilizerPos, waterPos)
    lights = newVersion(waters, waterPos, lightPos)
    temperatures = newVersion(lights, lightPos, temperaturePos)
    humidities = newVersion(temperatures, temperaturePos, humidityPos)
    location = newVersion(humidities, humidityPos, locationPos)
    print(min(location)) 
    
    return

def newVersion(list, start, end):
    newList = []
    for x in list:
        newList.append(map(x, checkMap(x, getMap(start, end))))
    return newList

def getMap(start, end):
    list = []
    for i in range(start, end - 2):
        list.append(input[i].strip("\n").split(" "))
    return list

def checkMap(input, maps):
    input = int(input)
    for map in maps: 
        if int(map[1]) <= input < int(map[1]) + int(map[2]):
            return map

def map(input, info):
    if info == None:
        return int(input)
    if int(info[1]) <= int(input) < int(info[1]) + int(info[2]):
        return (int(input) - int(info[1]) + int(info[0]))

main()