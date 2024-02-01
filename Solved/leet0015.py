# 15. 3Sum

def threeSum(nums: list[int]) -> list[list[int]]:
    output = []
    nums = sorted(nums)
    for k in range(len(nums)):
        if k != 0 and nums[k] == nums[k - 1]: continue
        for i in range(k + 1, len(nums)):
            if i != k + 1 and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, len(nums)):
                if j != i + 1 and nums[j] == nums[j - 1]: continue
                if nums[k] + nums[i] + nums[j] == 0: output.append([nums[k], nums[i], nums[j]])
    return output


print(threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
print(threeSum([0,1,1]))          # []
print(threeSum([0,0,0]))          # [[0,0,0]]
print(threeSum([0,0,0,0]))        # [[0,0,0]]
