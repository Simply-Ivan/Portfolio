
'''
Find Closest Number to Zero
'''

nums = [-4,-2,1,4,8]

def findClosestNumber(nums):
    closest = abs(nums[0])
    for i in range(1, len(nums)):
            
        if closest > abs(nums[i]):
            closest = abs(nums[i])
            
    return closest

print(findClosestNumber(nums))