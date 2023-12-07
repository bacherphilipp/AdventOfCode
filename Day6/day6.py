import re


#part1
data = open("C:/Users/phili/OneDrive/Desktop/AdventOfCode/Day6/input.txt", "r").read().split("\n")
time = re.findall(r'\d+', data[0])
distance = re.findall(r'\d+', data[1])

result = 1
for t, dist in zip(time, distance):
    t=int(t)
    waysToWin=0
    for i in range(0, int(t)+1):
         if i * (t - i ) > int(dist):
            waysToWin+=1
    result *= waysToWin

print("Part 1: " + str(result))

#part2
data = open("C:/Users/phili/OneDrive/Desktop/AdventOfCode/Day6/input.txt", "r").read().split("\n")
time = int(data[0][data[0].find(':')+1:].replace(' ', ''))
distance = int(data[1][data[1].find(':')+1:].replace(' ', ''))

result = 0
for i in range(0, time+1):
    if i * (time - i ) > int(distance):
        result+=1

print("Part 2: " + str(result))
