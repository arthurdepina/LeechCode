# 242. Valid Anagram

from collections import Counter

def isAnagram(s, t) -> bool:
    return Counter(s) == Counter(t)


print(isAnagram("anagram", "nagaram")) # true
print(isAnagram("rat", "car"))         # false
