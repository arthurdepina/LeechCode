# 11. Container With Most Water


def maxArea(height: list[int]) -> int:
    area, l, r = 0, 0, len(height) - 1

    while l < r:
        area = max(area, min(height[l], height[r]) * (r - l))

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    
    return area

print(maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(maxArea([1,1]))               #  1
print(maxArea([1,2,1]))             #  2
print(maxArea([4,3,2,1,4]))         # 16
