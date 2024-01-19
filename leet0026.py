"""
26. Remove Duplicates from Sorted Array
"""

def removeDuplicates(nums) -> int:
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j
 

# print(removeDuplicates([1,1,2])) # returns 2 -- nums will be [1, 2]
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # returns 5 -- nums will be [0,1,2,3,4,_,_,_,_,_]
                                               # in this particular solution,
                                               # nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
                                               # in the previous commited solution:
                                               # nums = [0, 1, 2, 3, 4]
