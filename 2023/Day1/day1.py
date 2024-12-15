def find(str, mode):
    digitList=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    ind = (9999,-1)
    for i,digit in enumerate(digitList):
        if mode==1:
            digit=digit[::-1]
        foundInd = str.find(digit)
        if foundInd != -1 and foundInd < ind[0]:
            ind = (foundInd,i+1)
    return ind

file1 = open('C:/Users/phili/OneDrive/Desktop/AdventOfCode/Day1/input.txt', 'r')
lines = file1.readlines()
sum = 0

for line in lines:
    res=""
    ind = find(line, 0)
    for i,char in enumerate([*line]):
          if char.isdigit():
            if(ind[0] != -1 and i<ind[0]):
                res=char
            else:
                res=str(ind[1])
            break
    
    ind = find(line[::-1], 1)
    for i,char in enumerate(reversed([*line])):
        if char.isdigit():
            if(ind[0] != -1 and i<ind[0]):
                res+=char
            else:
                res+=str(ind[1])
            break
    sum+= int(res)
    
print(sum)



