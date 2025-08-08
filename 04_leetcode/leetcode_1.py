
'''
Two Sum
'''

nums = [2,1,5,3]

target = 4

def two_sum(nums, target):
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]
            
            if sum == target:
                return [i, j]
                
print(two_sum(nums,target))

