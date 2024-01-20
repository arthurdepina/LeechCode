# 58. Length of Last Word

def lengthOfLastWord(s) -> int:
    s = s.split()
    return len(s[-1])


print(lengthOfLastWord("luffy is still joyboy"))


# A resposta abaixo também é interessante e
# deve ser mais rápida. Bom para não depender
# de métodos específicos disponíveis no Python

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length
