file = open('C:/Users/phili/OneDrive/Desktop/AdventOfCode/Day3/input.txt', 'r')
lines = file.readlines()

prevLine = None
result = 0

for id, line in enumerate(lines):

    if id+1<len(lines):
        nextLine = lines[id+1]
    else:
        nextLine = None

    digitStart = None
    charList = [*line]
    charListNext = []
    charListPrev = []
    if nextLine != None:
        charListNext = [*nextLine]
    else:
        charListNext = [*'.'* 500]
    if prevLine != None:
        charListPrev = [*prevLine]
    else:
        charListPrev = [*'.'* 500]

    res=''
    for i, char in enumerate(charList):
        if char.isdigit():
            if digitStart == None:
                digitStart = i
            res+=char
        elif digitStart != None:
            #print(charList[digitStart-1:i],charListPrev[digitStart-1:i],charListNext[digitStart-1:i])
            zipInput = None
            if digitStart==0:
                zipInput = zip(charList[digitStart:i+1],charListPrev[digitStart:i+1],charListNext[digitStart:i+1])
            else:
                zipInput = zip(charList[digitStart-1:i+1],charListPrev[digitStart-1:i+1],charListNext[digitStart-1:i+1])
        
            for chars in zipInput:
                if not chars[0].isalnum() and chars[0] != '.':
                    print(res)
                    result += int(res)
                elif not chars[1].isalnum() and chars[1] != '.':
                    print(res)
                    result += int(res)
                elif not chars[2].isalnum() and chars[2] != '.':
                    print(res)
                    result += int(res)
            digitStart = None
            res=''

    prevLine = line

print(result)