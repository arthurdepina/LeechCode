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

    # Em seguida o objetivo será fazer ‘loops’ aninhados. Um que remove os caracteres da palavra
    # de trás para frente (<-) e outro que remove da frente para trás (->); a cada iteração
    # comparando com as outras palavras do array, para encontrar uma repetição

    found = ""

    smallest_a = smallest
    smallest_b = smallest
    smallest_c = smallest

    for i in smallest_a:
        for s in strs:
            if smallest_a in s:
                found = smallest_a
            else:
                found = ""
        smallest_a = smallest_a[:-1]

    for j in smallest_b:
        for s in strs:
            if smallest_b in s and len(smallest_b) > len(found):
                found = smallest_b
            else:
                found = ""
        smallest_b = smallest_b[1:]

    for k in smallest_c:
        for s in strs:
            if smallest_c in s and len(smallest_c) > len(found):
                found = smallest_c
            else:
                found = ""
        smallest_c = smallest_c[:-1]
        smallest_c = smallest_c[1:]

    return found


print(longestCommonPrefix(["flower", "flow", "flight"]))  # Should return "fl"
"""
print(longestCommonPrefix(["dog", "racecar", "car"]))  # Should return ""
print(longestCommonPrefix(["lag", "staggering", "faggot"]))  # Should return "ag"
"""
