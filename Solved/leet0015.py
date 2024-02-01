# 15. 3Sum

def threeSum(nums: list[int]) -> list[list[int]]:
    output = []
    nums = sorted(nums)
    for a in range(len(nums)):
        if a != 0 and nums[a] == nums[a - 1]: continue
        b = a + 1
        c = len(nums) - 1
        while b < c:
            if b != a + 1 and nums[b] == nums[b - 1]:
                b += 1
                continue
            if c != len(nums) - 1 and nums[c] == nums[c + 1]:
                c -= 1
                continue
            if nums[a] + nums[b] + nums[c] == 0:
                output.append([nums[a], nums[b], nums[c]])
                if b != len(nums) and c != 0:
                    b += 1
                    c -= 1
                else:
                    break 
            if nums[a] + nums[b] + nums[c] < 0: b += 1
            if nums[a] + nums[b] + nums[c] > 0: c -= 1
    return output

 
print(threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
print(threeSum([0,1,1]))          # []
print(threeSum([0,0,0]))          # [[0,0,0]]
print(threeSum([0,0,0,0]))        # [[0,0,0]]
print(threeSum([-2,0,0,2,2]))     # [[-2,0,2]]
print(threeSum([-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]))
