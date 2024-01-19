# 242. Valid Anagram

from collections import Counter

def isAnagram(s, t) -> bool:
    return Counter(s) == Counter(t)


print(isAnagram("anagram", "nagaram")) # true
print(isAnagram("rat", "car"))         # false


# I also really liked the following solution:

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        char_map = [0] * 26

        for i in range(len(s)):
            char_map[ord(s[i]) - ord('a')] += 1
            char_map[ord(t[i]) - ord('a')] -= 1

        return all(count == 0 for count in char_map)
        
# the explanation available on:
#
# https://leetcode.com/problems/valid-anagram/solutions/
# 4410440/beats-100-explained-with-video-hashing-c-java-
# python-js-visualized/