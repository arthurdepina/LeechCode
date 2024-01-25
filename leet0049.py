# 49. Group Anagrams


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # strs = sorted(strs)
    anagrams = dict()
    for word in strs:
        s_word = ''.join(sorted(word))
        if s_word in list(anagrams.keys()):
            anagrams[s_word] += [word]
        else:
            anagrams[s_word] = [word]
    return list(anagrams.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
# print(groupAnagrams([""]))                                  # [[""]]
# print(groupAnagrams(["a"]))                                 # [["a"]]
