file = open('C:/Users/phili/OneDrive/Desktop/AdventOfCode/Day3/input.txt', 'r')
lines = file.readlines()

prevLine = None
result = 0

#Part 1
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
            zipInput = None
            if digitStart==0:
                zipInput = zip(charList[digitStart:i+1],charListPrev[digitStart:i+1],charListNext[digitStart:i+1])
            else:
                zipInput = zip(charList[digitStart-1:i+1],charListPrev[digitStart-1:i+1],charListNext[digitStart-1:i+1])
        
            for chars in zipInput:
                if not chars[0].isalnum() and chars[0] != '.' and chars[0] != '\n':
                    result += int(res)
                elif not chars[1].isalnum() and chars[1] != '.' and chars[1] != '\n':
                    result += int(res)
                elif not chars[2].isalnum() and chars[2] != '.' and chars[2] != '\n':
                    result += int(res)
            
            digitStart = None
            res=''

    prevLine = line
print(result)


file = open('C:/Users/phili/OneDrive/Desktop/AdventOfCode/Day3/input.txt', 'r')
lines = file.readlines()
prevLine = None
result = 0
#Part 2
def findNumbers(line):
    tupleList=[]
    sameNum=True
    number=''
    indList = []
    for i, c in enumerate(line):
        if c.isdigit():
            if(sameNum):
                number+=c
                indList.append(i)
            else:
                tupleList.append( (int(number),indList) )
                number=''
                indList = []
                number+=c
                indList.append(i)
            sameNum=True
        elif number != '':
            sameNum = False
    if number != '':
        tupleList.append( (int(number),indList) )
    return tupleList



for id, line in enumerate(lines):

    if id+1<len(lines):
        nextLine = lines[id+1]
    else:
        nextLine = None

    currentLineNumbers = findNumbers(line)
    prevLineNumbers = findNumbers(prevLine) if prevLine != None else []
    nextLineNumbers = findNumbers(nextLine) if nextLine != None else []
    gearSymbols = [i for i, letter in enumerate(line) if letter == '*']
    

    for gear in gearSymbols:
        occurences = 0
        res = 1
        for numberT in currentLineNumbers:
            if gear-1 in numberT[1]:
                occurences += 1
                res *= numberT[0]
            elif gear+1 in numberT[1]:
                occurences += 1
                res *= numberT[0]
        for numberT in nextLineNumbers:
            if gear-1 in numberT[1]:
                occurences += 1
                res *= numberT[0]
            elif gear+1 in numberT[1]:
                occurences += 1
                res *= numberT[0]
            elif gear in numberT[1]:
                occurences += 1
                res *= numberT[0]

        for numberT in prevLineNumbers:
            if gear-1 in numberT[1]:
                occurences += 1
                res *= numberT[0]
            elif gear+1 in numberT[1]:
                occurences += 1
                res *= numberT[0]
            elif gear in numberT[1]:
                occurences += 1
                res *= numberT[0]

        if occurences==2 and res > 1:
            result += res


    prevLine = line
print(result)