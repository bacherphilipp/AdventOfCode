import re

#Part 1
file = open("input.txt", "r")
result = 0
for line in file:
    res=0
    line = line[line.find(':')+1:].split('|')
    winningNums = [int(n) for n in re.findall(r'\d+', line[0])]
    pickedNums = [int(n) for n in re.findall(r'\d+', line[1])]

    for num in pickedNums:
        if num in winningNums:
            if res == 0:
                res = 1
            else:
                res*=2
    result+= res
print("Part 1 " + str(result))

#Part 2
file = open("input.txt", "r")
result = 0
cardCount = dict(zip([i for i in range(1, 210)], [0 for i in range(1, 210)]))
for i, line in enumerate(file,1):
    cardCount[i]+=1
    line = line[line.find(':')+1:].split('|')
    winningNums = [int(n) for n in re.findall(r'\d+', line[0])]
    pickedNums = [int(n) for n in re.findall(r'\d+', line[1])]

    j=0
    res=0
    for num in pickedNums:
        if num in winningNums:
            res+=1
            cardCount[i+res]+=cardCount[i]
        
print("Part 2: " + str(sum(cardCount.values())))
