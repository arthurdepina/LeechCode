# 128. Longest Consecutive Sequence

def longestConsecutive(nums: list[int]) -> int:
    nums_set = set(nums)
    length_longest = 0

    for i in nums:
        if i - 1 not in nums_set:
            current_length = 1
            while i + current_length in nums_set:
                current_length += 1
            length_longest = max(length_longest, current_length)
    
    return length_longest


print(longestConsecutive([100,4,200,1,3,2])) # 4
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9
