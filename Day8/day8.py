import math

def kgv(zahlen):
    kgv = zahlen[0]
    for zahl in zahlen[1:]:
        kgv = abs(kgv * zahl) // math.gcd(kgv, zahl)
    return kgv

data = open("C:/Users/phili/OneDrive/Desktop/AdventOfCode/Day8/input.txt", "r").read().split("\n")

direction = data[0]
coords = dict()
start='AAA'

for i, coord in enumerate(data[2:]):
    coords[coord[:3]] = (coord[7:10], coord[12:15])

iterator = iter(direction)
result = 0
while(start != 'ZZZ'):
    LR = next(iterator, None)
    if LR is None:
        iterator = iter(direction)
        LR = next(iterator, None)
    start = coords[start][0 if LR == 'L' else 1]
    result+=1
print("Part 1: " + str(result))

#part 2

starts=[d[:3] for d in data[2:] if d[:3].endswith('A')]
result = []
for i,start in enumerate(starts):
    count=0
    while(not start.endswith('Z')):
        LR = next(iterator, None)
        if LR is None:
            iterator = iter(direction)
            LR = next(iterator, None)
        start = coords[start][0 if LR == 'L' else 1]
        count+=1
    result.append(count)        

print("Part 2: " + str(kgv(result)))
