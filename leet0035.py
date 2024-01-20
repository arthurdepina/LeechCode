# 35. Search Insert Position


def searchInsert(nums, target) -> int:
    start = 0
    ending = len(nums)
    while True:

        if nums[ending - 1] < target: return ending
        if nums[start] > target: return start
        
        i_current = (start + ending)//2

        if nums[i_current] == target: return i_current
        else:
            if nums[i_current] > target: ending = i_current
            else: start = i_current


print(searchInsert([1, 3, 5, 6], 2))
