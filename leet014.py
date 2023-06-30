"""
Write a function to find the longest common prefix string amongst an array of strings.
If there's no common prefix, return an empty string ""
"""


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
