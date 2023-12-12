with open('./5_garden/input.txt', 'r') as file:
    input = file.readlines()

def main():
    seeds = input[0].removeprefix("seeds: ").strip().split(' ')
    
    newSeeds = []
    for i in range(len(seeds)):
        if i % 2 == 0 and seeds[i+1] != None: 
            start = int(seeds[i])
            for i in range(start, start + int(seeds[i+1])):
                newSeeds.append(i)
    
    seedPos = (input.index("seed-to-soil map:\n")) + 1
    soilPos = (input.index("soil-to-fertilizer map:\n")) + 1
    fertilizerPos = (input.index("fertilizer-to-water map:\n")) + 1
    waterPos = (input.index("water-to-light map:\n")) + 1
    lightPos = (input.index("light-to-temperature map:\n")) + 1
    temperaturePos = (input.index("temperature-to-humidity map:\n")) + 1
    humidityPos = (input.index("humidity-to-location map:\n")) + 1
    locationPos = len(input) - 1 + 2
    
    soils = []
    for seed in newSeeds:
        soils.append(map(seed, checkMap(seed, getMap(seedPos, soilPos))))
    # print(soils)
    
    fertilizers = []
    for soil in soils: 
        fertilizers.append((map(soil, checkMap(soil, getMap(soilPos, fertilizerPos)))))
    # print(fertilizers)
    
    waters = []
    for fertilizer in fertilizers: 
        waters.append(map(fertilizer, checkMap(fertilizer, getMap(fertilizerPos, waterPos))))
    # print(waters)
    
    lights = []
    for water in waters: 
        lights.append((map(water, checkMap(water, getMap(waterPos, lightPos)))))
    # print(lights)
    
    temperatures = []
    for light in lights: 
        temperatures.append((map(light, checkMap(light, getMap(lightPos, temperaturePos)))))
    # print(temperatures)
    
    humidities = []
    for temperature in temperatures: 
        humidities.append((map(temperature, checkMap(temperature, getMap(temperaturePos, humidityPos)))))
    # print(humidities)
    
    location = []
    for humidity in humidities: 
        location.append((map(humidity, checkMap(humidity, getMap(humidityPos, locationPos)))))
    # print(location)
    
    print(min(location))
    return

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