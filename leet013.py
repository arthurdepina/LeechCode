def romanToInt(s):
    rti = [["I", 1],
           ["V", 5],
           ["X", 10],
           ["L", 50],
           ["C", 100],
           ["D", 500],
           ["M", 1000]]
    s = list(s)
    for i in range(len(s)):
        pass


print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))