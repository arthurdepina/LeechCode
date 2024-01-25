# 35. Search Insert Position


def searchInsert(nums, target) -> int:

    start = 0
    ending = len(nums) - 1

    while start <= ending:
        i_current = (start + ending)//2
        if nums[i_current] == target: return i_current
        if nums[i_current] > target: ending = i_current - 1
        else: start = i_current + 1

    return start


print(searchInsert([1,2,4,6,7], 3))
