# 03. Longest Substring Without Repeating Characters


def lengthOfLongestSubstring(s: str) -> int:
    chars  = set()
    l      = 0
    length = 0

    for r in range(len(s)):
        while s[r] in chars:
            chars.remove(s[l])
            l += 1
        chars.add(s[r])
        length = max(length, r - l + 1)

    return length


print(lengthOfLongestSubstring("abcabcbb")) # 3
print(lengthOfLongestSubstring("bbbbb"))    # 1
print(lengthOfLongestSubstring("pwwkew"))   # 3
