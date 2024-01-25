# 49. Group Anagrams

from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)

    for word in strs:
        s_word = ''.join(sorted(word))
        anagrams[s_word].append(word)
    
    return anagrams.values()


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
                 # [["bat"],["nat","tan"],["ate","eat","tea"]]
# print(groupAnagrams([""]))                         #  [[""]]
# print(groupAnagrams(["a"]))                        # [["a"]]
