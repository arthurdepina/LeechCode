# 238. Product of Array Except Self

from functools import reduce

def productExceptSelf(nums: list[int]) -> list[int]:
    length = len(nums)
    output = [1] * length
    if 0 in nums:
        if nums.count(0) > 1:
            return [0] * length
        else:
            index_0 = nums.index(0)
            for i in range(length):
                if i != index_0:
                    output[i] = 0
                else:
                    for j in range(length):
                        if j!=index_0: output[index_0] *= nums[j]
        return output
    m_all  = reduce((lambda x, y: x * y), nums)
    for i in range(len(output)):
        if nums[i] != 0: output[i] = m_all//nums[i]
    return output


print(productExceptSelf([1,2,3,4]))     # [24,12,8,6]
print(productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]
