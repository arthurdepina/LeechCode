# 58. Length of Last Word

def lengthOfLastWord(s) -> int:
    s = s.split()
    return len(s[-1])


print(lengthOfLastWord("luffy is still joyboy"))

