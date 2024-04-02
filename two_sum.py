nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return i, seen[diff]
        seen[nums[i]] = i
