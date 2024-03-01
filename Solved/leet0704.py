# 704. Binary Search


def search(nums: list[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    
    while start <= end:
        curr = (start + end) // 2
        if nums[curr] == target:
            return curr
        elif nums[curr] > target:
            end = curr - 1
        else:
            start = curr + 1
    
    return -1



print(search([-1,0,3,5,9,12], 9))   #  4
print(search([-1,0,3,5,9,12], 2))   # -1
