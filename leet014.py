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

    finder = False
    found = ""
    found_a = ""
    found_b = ""
    found_c = ""

    smallest_a = smallest
    smallest_b = smallest
    smallest_c = smallest

    for i in smallest_a:
        for s in strs:
            if smallest_a in s and len(smallest_a) > len(found_a):
                finder = True
                found_a = smallest_a
            elif smallest_a not in s:
                found_a = ""
                finder = False
        smallest_a = smallest_a[:-1]

    if finder:
        found = found_a

    for j in smallest_b:
        for s in strs:
            if smallest_b in s and len(smallest_b) > len(found_b):
                finder = True
                found_b = smallest_b
            elif smallest_b not in s:
                found_b = ""
                finder = False
        smallest_b = smallest_b[1:]

    if finder:
        found = found_b

    for k in smallest_c:
        for s in strs:
            if smallest_c in s and len(smallest_c) > len(found_c):
                finder = True
                found_c = smallest_c
            elif smallest_c not in s:
                found_c = ""
                finder = False
        smallest_c = smallest_c[:-1]
        smallest_c = smallest_c[1:]

    if finder:
        found = found_c

    return found


"""
print(longestCommonPrefix(["flower", "flow", "flight"]))  # Should return "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))  # Should return ""
"""
print(longestCommonPrefix(["lag", "staggering", "faggot"]))  # Should return "ag"

