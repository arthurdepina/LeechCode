# 49. Group Anagrams

from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)

    for word in strs:
        count = [0] * 26
        for letter in word:
            count[ord(letter) - ord('a')] += 1
        anagrams[tuple(count)].append(word)
    
    return anagrams.values()


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
                 # [["bat"],["nat","tan"],["ate","eat","tea"]]
# print(groupAnagrams([""]))                         #  [[""]]
# print(groupAnagrams(["a"]))                        # [["a"]]
