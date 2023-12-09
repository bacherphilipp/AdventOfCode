data = open("C:/Users/phili/OneDrive/Desktop/AdventOfCode/Day9/input.txt", "r").readlines()

def func(nums):
    if nums.count(0) == len(nums):
        return 0
    buf=[]
    for i,num in enumerate(nums):
        if i == len(nums)-1:
            break
        buf.append(nums[i+1]-num)
    return func(buf) + nums[len(nums)-1]

resultP1 = 0
resultP2=0
for line in data:
    res = []
    nums = [int(num) for num in line.split()]
    resultP1+=func(nums)
    resultP2+=func(list(reversed(nums)))
        
print("Part 1: " + str(resultP1))
print("Part 2: " + str(resultP2))

