"""
26. Remove Duplicates from Sorted Array
"""

def removeDuplicates(nums) -> int:
    index = 1
    k = len(nums)
    while index <= k - 1:
        if nums[index] == nums[index - 1]:
            del nums[index]
            k -= 1
        else:
            index += 1
    print(nums)
    return k

 

# print(removeDuplicates([1,1,2])) # returns 2 -- nums will be [1, 2]
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # returns 5 -- nums will be [0,1,2,3,4,_,_,_,_,_]
