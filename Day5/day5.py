import sys

def arrToInt(arr):
    array_of_ints = []
    for subarray in arr:
        int_subarray = []
        for element in subarray:
            if element:  # Check if the string is not empty
                int_subarray.append(int(element))
        array_of_ints.append(int_subarray)
    return array_of_ints


def findDest(arr, source):
    dest = None
    for target in arr:
        #target = list(map(int, target))
        if target[1] <= source < target[1] + target[2]:
            dest = target[0] + ( source - target[1])
            break
    return source if dest is None else dest

lowestDest = sys.maxsize

data = open("input.txt", "r").read().split("\n\n")
splitData = map(lambda b: [a.split(" ") for a in b[b.find(":")+2:].split("\n") ] ,data)
seeds = arrToInt(next(splitData))
seedToSoil = arrToInt(next(splitData))
soilToFert = arrToInt(next(splitData))
fertToWater= arrToInt(next(splitData))
waterToLight = arrToInt(next(splitData))
lightToTemp = arrToInt(next(splitData))
tempToHumidity = arrToInt(next(splitData))
humidityToLoc = arrToInt(next(splitData))

for seed in seeds[0]:
    res = findDest(humidityToLoc,(findDest(tempToHumidity,(findDest(lightToTemp,(findDest(waterToLight,(findDest(fertToWater,(findDest(soilToFert,(findDest(seedToSoil, int(seed))))))))))))))
    lowestDest = res if res < lowestDest else lowestDest

print("Part 1: "  + str(lowestDest))

lowestDest = sys.maxsize
for i,seed in enumerate(seeds[0]):
    if i%2==0:
        for seed in range(int(seeds[0][i]), int(seeds[0][i])+int(seeds[0][i+1])):
            res = findDest(humidityToLoc,(findDest(tempToHumidity,(findDest(lightToTemp,(findDest(waterToLight,(findDest(fertToWater,(findDest(soilToFert,(findDest(seedToSoil, seed)))))))))))))
            lowestDest = res if res < lowestDest else lowestDest
    print("progressing..")

print("Part 2: "  + str(lowestDest))