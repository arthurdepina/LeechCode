# 014 Longest Common Prefix


def longestCommonPrefix(strs):
    strs = sorted(strs)
    answer = ""
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return answer
        answer += first[i]
    return answer


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["reflower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))

# Versão aprimorada: https://leetcode.com/problems/longest-common-prefix/solutions/3273176/python3-c-java-19-ms-beats-99-91/
