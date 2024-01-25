# 347. Top K Frequent Elements

from collections import defaultdict

def topKFrequent(nums: list[int], k: int) -> list[int]:
    freqs = defaultdict(int)

    for num in nums:
        freqs[num] += 1

    return sorted(freqs, key=freqs.get, reverse=True)[:k]


print(topKFrequent([1,1,1,2,2,3], 2))       # [1,2]
print(topKFrequent([1], 1))                 # [1]
