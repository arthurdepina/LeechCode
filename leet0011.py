# 11. Container With Most Water


def maxArea(height: list[int]) -> int:
    i = 0
    min_height = min(height[i], height[- 1])
    max_area = min_height * (len(height) - 1 - i)
    while i < len(height) - 1:
        for j in range(len(height) - 1, i, -1):
            if height[j] < min_height:
                continue
            cur_min_height = min(height[i], height[j])
            cur_area       = cur_min_height * (j - i)
            if max(max_area, cur_area) == cur_area:
                max_area   = cur_area
                min_height = cur_min_height
        i += 1
    return max_area


print(maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(maxArea([1,1]))               #  1
print(maxArea([1,2,1]))             #  2
print(maxArea([4,3,2,1,4]))         # 16
