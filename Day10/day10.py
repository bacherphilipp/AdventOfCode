import numpy as np
import time

def findStartStep(pipes, start):
    if pipes[start[0]][start[1]+1] == '-' or pipes[start[0]][start[1]+1] == 'J' or pipes[start[0]][start[1]+1] == '7':
        return tuple((start[0], start[1]+1))
    elif pipes[start[0]][start[1]-1] == '-' or pipes[start[0]][start[1]-1] == 'L' or pipes[start[0]][start[1]-1] == 'F':
        return tuple((start[0], start[1]-1))
    elif pipes[start[0]-1][start[1]] == '|' or pipes[start[0]-1][start[1]] == '7' or  pipes[start[0]-1][start[1]] == 'F':
        return tuple((start[0]-1, start[1]))
    elif pipes[start[0]+1][ start[1]] == '|' or pipes[start[0]+1][start[1]] == 'J' or  pipes[start[0]+1][start[1]] == 'L':
        return tuple((start[0]+1, start[1]))


with open("C:/Users/phili/OneDrive/Desktop/AdventOfCode/Day10/input.txt") as file:
    lines = [[char for char in row if char != '\n'] for row in [[*line] for line in file]]

start = tuple(np.argwhere(np.array(lines) == 'S')[0])
totalPath=[]
totalPath.append(start)
currentPos = findStartStep(lines, start)
prevPos = start
pathLength=1
while lines[currentPos[0]][currentPos[1]] != 'S':
    totalPath.append(currentPos)
    if lines[currentPos[0]][currentPos[1]] == '|':
        if prevPos[0] < currentPos[0]:
            prevPos=currentPos
            currentPos = (currentPos[0]+1, currentPos[1])
        else:
            prevPos=currentPos
            currentPos = (currentPos[0]-1, currentPos[1])
    elif lines[currentPos[0]][currentPos[1]] == '-':
        if prevPos[1] < currentPos[1]:
            prevPos=currentPos
            currentPos = (currentPos[0], currentPos[1]+1)
        else:
            prevPos=currentPos
            currentPos = (currentPos[0], currentPos[1]-1)
    elif lines[currentPos[0]][currentPos[1]] == 'L':
        if prevPos[1]>currentPos[1]:
            prevPos=currentPos
            currentPos = (currentPos[0]-1, currentPos[1])
        else:
            prevPos=currentPos
            currentPos = (currentPos[0], currentPos[1]+1)
    elif lines[currentPos[0]][currentPos[1]] == 'J':
        if prevPos[1]<currentPos[1]:
            prevPos=currentPos
            currentPos = (currentPos[0]-1, currentPos[1])
        else: 
            prevPos=currentPos
            currentPos = (currentPos[0], currentPos[1]-1)
    elif lines[currentPos[0]][currentPos[1]] == '7':
        if prevPos[1]<currentPos[1]:
            prevPos=currentPos
            currentPos = (currentPos[0]+1, currentPos[1])
        else:
            prevPos=currentPos
            currentPos = (currentPos[0], currentPos[1]-1)
    elif lines[currentPos[0]][currentPos[1]] == 'F':
        if prevPos[1]>currentPos[1]:
            prevPos=currentPos
            currentPos = (currentPos[0]+1, currentPos[1])
        else:
            prevPos=currentPos
            currentPos = (currentPos[0], currentPos[1]+1)
    pathLength+=1

print("Part 1: " + str(int(pathLength/2)))

#print(totalPath)

#part2
# vol=0
# count=0
# prevHit=()
# for i,lineX in enumerate(lines):
#     for j,pos in enumerate(lineX):
#         if(i,j) in totalPath:
#             ind = totalPath.index((i,j))
#             if ind > 0:
#                 if totalPath[ind-1] == prevHit:
#                     count=0
#                     prevHit=(i,j)
#                     continue
#             count = 0 if count==1 else 1
#             prevHit=(i,j)
#         else:
#             if count == 1:
#                 print((i,j))
#                 vol+=1
#         #print(pos)

vol=0
count=0
isInline=0
for i, lineX in enumerate(lines):
    for j, pos in enumerate(lineX):
        if(i,j) in totalPath:
            if ( (i,j+1) in totalPath and abs(totalPath.index((i,j+1)) - totalPath.index((i,j))) == 1 ) or ( (i,j-1) in totalPath and  abs(totalPath.index((i,j)) - totalPath.index((i,j-1))) == 1 ):
                print("test", (i,j))
                #count=0
                isInline=1
                continue
            isEnc=0
            count = 0 if count==1 else 1
            print((i,j), count)
        else:
            if count == 1 and isInline == 0:
                print("Hit on: ",(i,j))
                vol+=1
    count=0
print(vol)

for i, lineX in enumerate(lines):
    for j, pos in enumerate(lineX):
        if (i,j) in totalPath:
            print('\033[95m' + pos + '\033[0m', end="")
        else:
            print(pos, end="")
    print("")