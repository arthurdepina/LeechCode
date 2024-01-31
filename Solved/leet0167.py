# 167. Two Sum II - Input Array Is Sorted

def twoSum(numbers: list[int], target: list[int]) -> list[int]:
    for i in range(len(numbers)):
        if numbers[i] == numbers[i - 1]: continue
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]


# print(twoSum([2,7,11,15], 9)) # [1,2]
# print(twoSum([2,3,4], 6))     # [1,3]
# print(twoSum([-1,0], -1))     # [1,2]


def twoSumTwoPointer(numbers: list[int], target: list[int]) -> list[int]: # 84%
    a = 0
    b = len(numbers) - 1
    while a < b:
        if numbers[a] + numbers[b] <  target: a += 1
        if numbers[a] + numbers[b] >  target: b -= 1
        if numbers[a] + numbers[b] == target: return [a + 1, b + 1]


print(twoSumTwoPointer([2,7,11,15], 9)) # [1,2]
print(twoSumTwoPointer([2,3,4], 6))     # [1,3]
print(twoSumTwoPointer([-1,0], -1))     # [1,2]
