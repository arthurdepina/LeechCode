# 028. Find the Index of the First Occurrence in a String 

def strStr(haystack, needle) -> int:
    return haystack.find(needle)


print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))
