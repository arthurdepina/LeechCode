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

    found = False

    for i in range(len(smallest)//2 - 1):
        for word in strs:
            if smallest in word:
                found = True
            else:
                found = False
        if found:
            return smallest
        else:
            smallest = smallest[:-1]
        for j in range(len(smallest)//2):
            for word in strs:
                if smallest in word:
                    found = True
                else:
                    found = False
            if found:
                return smallest
            else:
                smallest = smallest[1:]


print(longestCommonPrefix(["flower", "flow", "flight"]))  # Should return "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))  # Should return ""
print(longestCommonPrefix(["lag", "staggering", "faggot"]))  # Should return "ag"

