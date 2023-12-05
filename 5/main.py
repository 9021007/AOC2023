import os
from tqdm import tqdm

input = open("exampleinput.txt", "r").read().split("\n")
# input = open("input.txt", "r").read().split("\n")



# destination range start, the source range start, range length.

soilmaps = [
        # {
        #     "start": 0,
        #     "length": 0,
        #     "offset": 0,
        # }
    ]

# seed-to-soil map:
# soil-to-fertilizer map:
# fertilizer-to-water map:
# water-to-light map:
# light-to-temperature map:
# temperature-to-humidity map:
# humidity-to-location map:



soildata = input[input.index("seed-to-soil map:") + 1:input.index("soil-to-fertilizer map:") - 1]
for i in range(len(soildata)):
    soildata[i] = soildata[i].split(" ")
    soilmaps.append({
        "start": int(soildata[i][1]),
        "length": int(soildata[i][2]),
        "offset": int(soildata[i][0])-int(soildata[i][1]),
    })

# print(soilmaps)

def getSoil(seed):
    for i in range(len(soilmaps)):
        if seed >= soilmaps[i]["start"] and seed < soilmaps[i]["start"] + soilmaps[i]["length"]:
            return seed + soilmaps[i]["offset"]            
    return seed

# print(getSoil(13))

fertilizermaps = []

fertilizerdata = input[input.index("soil-to-fertilizer map:") + 1:input.index("fertilizer-to-water map:") - 1]
for i in range(len(fertilizerdata)):
    fertilizerdata[i] = fertilizerdata[i].split(" ")
    fertilizermaps.append({
        "start": int(fertilizerdata[i][1]),
        "length": int(fertilizerdata[i][2]),
        "offset": int(fertilizerdata[i][0])-int(fertilizerdata[i][1]),
    })

# print(fertilizermaps)

def getFertilizer(soil):
    for i in range(len(fertilizermaps)):
        if soil >= fertilizermaps[i]["start"] and soil < fertilizermaps[i]["start"] + fertilizermaps[i]["length"]:
            return soil + fertilizermaps[i]["offset"]            
    return soil

# print(getFertilizer(81))

watermaps = []

waterdata = input[input.index("fertilizer-to-water map:") + 1:input.index("water-to-light map:") - 1]
for i in range(len(waterdata)):
    waterdata[i] = waterdata[i].split(" ")
    watermaps.append({
        "start": int(waterdata[i][1]),
        "length": int(waterdata[i][2]),
        "offset": int(waterdata[i][0])-int(waterdata[i][1]),
    })

# print(watermaps)

def getWater(fertilizer):
    for i in range(len(watermaps)):
        if fertilizer >= watermaps[i]["start"] and fertilizer < watermaps[i]["start"] + watermaps[i]["length"]:
            return fertilizer + watermaps[i]["offset"]            
    return fertilizer

# print(getWater(81))

lightmaps = []

lightdata = input[input.index("water-to-light map:") + 1:input.index("light-to-temperature map:") - 1]
for i in range(len(lightdata)):
    lightdata[i] = lightdata[i].split(" ")
    lightmaps.append({
        "start": int(lightdata[i][1]),
        "length": int(lightdata[i][2]),
        "offset": int(lightdata[i][0])-int(lightdata[i][1]),
    })

# print(lightmaps)

def getLight(water):
    for i in range(len(lightmaps)):
        if water >= lightmaps[i]["start"] and water < lightmaps[i]["start"] + lightmaps[i]["length"]:
            return water + lightmaps[i]["offset"]            
    return water

# print(getLight(81))

temperaturemaps = []

temperaturedata = input[input.index("light-to-temperature map:") + 1:input.index("temperature-to-humidity map:") - 1]
for i in range(len(temperaturedata)):
    temperaturedata[i] = temperaturedata[i].split(" ")
    temperaturemaps.append({
        "start": int(temperaturedata[i][1]),
        "length": int(temperaturedata[i][2]),
        "offset": int(temperaturedata[i][0])-int(temperaturedata[i][1]),
    })

# print(temperaturemaps)

def getTemperature(light):
    for i in range(len(temperaturemaps)):
        if light >= temperaturemaps[i]["start"] and light < temperaturemaps[i]["start"] + temperaturemaps[i]["length"]:
            return light + temperaturemaps[i]["offset"]            
    return light

# print(getTemperature(81))

humiditymaps = []

humiditydata = input[input.index("temperature-to-humidity map:") + 1:input.index("humidity-to-location map:") - 1]
for i in range(len(humiditydata)):
    humiditydata[i] = humiditydata[i].split(" ")
    humiditymaps.append({
        "start": int(humiditydata[i][1]),
        "length": int(humiditydata[i][2]),
        "offset": int(humiditydata[i][0])-int(humiditydata[i][1]),
    })

# print(humiditymaps)

def getHumidity(temperature):
    for i in range(len(humiditymaps)):
        if temperature >= humiditymaps[i]["start"] and temperature < humiditymaps[i]["start"] + humiditymaps[i]["length"]:
            return temperature + humiditymaps[i]["offset"]            
    return temperature

# print(getHumidity(81))

locationmaps = []

locationdata = input[input.index("humidity-to-location map:") + 1:-1]
for i in range(len(locationdata)):
    locationdata[i] = locationdata[i].split(" ")
    locationmaps.append({
        "start": int(locationdata[i][1]),
        "length": int(locationdata[i][2]),
        "offset": int(locationdata[i][0])-int(locationdata[i][1]),
    })

# print(locationmaps)

def getLocation(humidity):
    for i in range(len(locationmaps)):
        if humidity >= locationmaps[i]["start"] and humidity < locationmaps[i]["start"] + locationmaps[i]["length"]:
            return humidity + locationmaps[i]["offset"]            
    return humidity

# print(getLocation(getHumidity(getTemperature(getLight(getWater(getFertilizer(getSoil(13))))))))
# print(getLocation(getHumidity(getTemperature(getLight(getWater(getFertilizer(getSoil(55))))))))

# print(getLocation(getHumidity(getTemperature(getLight(getWater(getFertilizer(getSoil(79))))))))

# print(getLocation(getHumidity(getTemperature(getLight(getWater(getFertilizer(getSoil(14))))))))

results = []
currentlowestloc = 999999999999999999999
currentlowestseed = 0

print("Calculating...")

tmpseeds = input[0][6:].split(" ")
seeds = []
seeds2 = []

for i in range(len(tmpseeds)):
    if tmpseeds[i] != "":
        seeds.append(int(tmpseeds[i]))

for i in range(len(seeds)):
    if i % 2 == 0:
        seeds2.append((seeds[i], seeds[i+1]))

seeds = []

for i in tqdm(range(len(seeds2))):
    for j in tqdm(range(seeds2[i][1])):

        if getLocation(getHumidity(getTemperature(getLight(getWater(getFertilizer(getSoil(seeds2[i][0] + j))))))) < currentlowestloc:
            currentlowestloc = getLocation(getHumidity(getTemperature(getLight(getWater(getFertilizer(getSoil(seeds2[i][0] + j)))))))
            currentlowestseed = seeds2[i][0] + j



print(currentlowestseed)
print(currentlowestloc)