# 217. Contains Duplicate

def containsDuplicate(nums) -> bool:
    return list(dict.fromkeys(nums)) != nums


print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
