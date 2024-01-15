# 217. Contains Duplicate

def containsDuplicate(nums) -> bool:
    contains = list()
    for i in nums:
        if i in contains:   
            return True
        contains.append(i)
    return False


# print(containsDuplicate([1,2,3,1]))
# print(containsDuplicate([1,2,3,4]))
# print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
