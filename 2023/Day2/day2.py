def findCount(input, str):
    ind=input.find(str)
    
    if ind>0:
        if ind>2 and input[ind-3].isdigit():
            sol = int(input[ind-3:ind-1])
            return sol if type(sol) is int else 1
        else:
            sol = int(input[ind-2])
            return sol if type(sol) is int else 1
    else:
        return 0

countRed = 12
countGreen = 13
countBlue = 14

file = open('C:/Users/phili/OneDrive/Desktop/AdventOfCode/Day2/input.txt', 'r')
lines = file.readlines()
result = 0

#Part One
for gameId, line in enumerate(lines):
    #strip game and id
    line = line[line.find(":") + 2:]
    turns = line.split(";")
    cont=True
    for turn in turns:
        nRed=findCount(turn, "red")
        nGreen=findCount(turn, "green")
        nBlue=findCount(turn, "blue")    
        if( nRed>countRed or nGreen>countGreen or nBlue>countBlue ):
            cont=False
            
    if cont:
        result+=gameId+1
print("Part 1: " + str(result))

#Part two
file = open('C:/Users/phili/OneDrive/Desktop/AdventOfCode/Day2/input.txt', 'r')
lines = file.readlines()
result = 0
for gameId, line in enumerate(lines):
    #strip game and id
    line = line[line.find(":") + 2:]
    turns = line.split(";")
    nRed = 0
    nGreen = 0
    nBlue = 0
    for turn in turns:
        res = findCount(turn, "red")
        if res >= nRed:
            nRed = res
        res=findCount(turn, "green")
        if res >= nGreen:
            nGreen = res
        res = findCount(turn, "blue")
        if res >= nBlue:
            nBlue = res
    result += nRed * nGreen * nBlue

print("Part 2: " + str(result))





    