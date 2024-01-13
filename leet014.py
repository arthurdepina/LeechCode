# 014 Longest Common Prefix


def longestCommonPrefix(strs):
    # Encontrando a menor palavra
    smallest = strs[0]
    for word in strs:
        if len(word) < len(smallest):
            smallest = word

    found = ""

    for i in smallest:
        for s in strs:
            if smallest in s[:len(smallest)] and len(smallest) > len(found):
                found = smallest
            elif smallest not in s[:len(smallest)]:
                found = ""
                break
        smallest = smallest[:-1]

    return found


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["reflower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))

# Versão aprimorada: https://leetcode.com/problems/longest-common-prefix/solutions/3273176/python3-c-java-19-ms-beats-99-91/
