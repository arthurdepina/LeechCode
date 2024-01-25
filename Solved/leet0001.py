# 001. Two Sum

def twoSum(nums, target):
    dictionary = dict()
    for i in range(len(nums)):
        if target - nums[i] in dictionary:
            return [dictionary[target - nums[i]], i]
        else:
            dictionary[nums[i]] = i
    return []


print(twoSum([2,7,11,15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))

#                   Brute Force Solution

# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i, len(nums) - 1):
#                 if nums[i] + nums[j + 1] == target:
#                     return [i, j + 1]
#             else:
#                 continue
