nums = [2, 7, 11, 15]
target = 9
complements = {}  
for i, num in enumerate(nums):
    complement = target - num
    if complement in complements:

        indices = [complements[complement], i]
        print(indices)
        break
    complements[num] = i
