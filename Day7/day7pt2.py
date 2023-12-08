from functools import cmp_to_key

possibleHands = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def compare(hand1, hand2):
    hand1=[*hand1[0]]
    hand2=[*hand2[0]]
    for card in zip(hand1, hand2):
        if(card[0]==card[1]):
            continue
        elif possibleHands.index(card[1]) <possibleHands.index(card[0]):
            return 1
        else:
            return -1
    return 0

lines = open('C:/Users/phili/OneDrive/Desktop/AdventOfCode/Day7/input.txt', 'r').readlines()

ranks=dict()
ranks['5pair'] = []
ranks['4pair'] = []
ranks['fullHouse'] = []
ranks['3pair'] = []
ranks['2pair'] = []
ranks['pair'] = []
ranks['highCard'] = []

for line in lines:
    cardDict = dict()
    for char in [*line[:line.find(' ')]]:
        #if(char!='J'):
        if char in cardDict:
            cardDict[char]+=1
        else:
            cardDict[char]=1

    handString = line[:5]
    jCount=None
    if 'J' in handString:
        jCount = handString.count('J')
    hand=(handString, line[6:].replace('\n', ''))
    values=cardDict.values()

    if 3 in values and 2 in values and 'J' in cardDict.keys():
        ranks['5pair'].append(hand)
        continue
    if 'J' in cardDict.keys():
        cardDict.pop('J')

    if 5 in values:
        ranks['5pair'].append(hand)
    elif 4 in values:
        if jCount:
            ranks['5pair'].append(hand)
        else:  
            ranks['4pair'].append(hand)
    elif 3 in values and 2 in values:
        ranks['fullHouse'].append(hand)
    elif 3 in values:
        if jCount:
            ranks[str(3+jCount)+'pair'].append(hand)
        else:
            ranks['3pair'].append(hand)
    elif list(values).count(2) == 2:
        if jCount:
            #ranks[str(2+jCount)+'pair'].append(hand)
            ranks['fullHouse'].append(hand)
        else:
            ranks['2pair'].append(hand)
    elif list(values).count(2) == 1:
        if jCount:
            ranks[str(2+jCount)+'pair'].append(hand)
        else:
            ranks['pair'].append(hand)
    else:
        if jCount==1:
            ranks['pair'].append(hand)
        elif jCount ==5:
            ranks['5pair'].append(hand)
        elif jCount != None and jCount>1:
            ranks[str(jCount+1)+'pair'].append(hand)
        else:
            ranks['highCard'].append(hand)

finalList=[]
for result in ranks.values():
    result.sort(key=cmp_to_key(compare))
    finalList.extend(result)

totalWinning=0
for i, item in enumerate(reversed(finalList)):
    totalWinning+=(int(item[1])*(i+1))

print('Part 2: ' + str(totalWinning))



