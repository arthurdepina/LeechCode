# 027. Remove Elements

def removeElement(nums, val) -> int:
    i = len(nums) - 1
    while i >= 0:
        if nums[i] == val:
            nums.pop(i)
        i -= 1
    print(nums)
    return len(nums)


print(removeElement([3,2,2,3], 3)) # 2, nums = [2,2,_,_]
print(removeElement([0,1,2,2,3,0,4,2], 2)) # 5, nums = [0,1,4,0,3,_,_,_]
