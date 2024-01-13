# 13. Roman to Integer

def romanToInt(s):
    x = 0
    rti = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    for i in range(len(s)):
        if i < len(s) - 1 and rti[s[i]] < rti[s[i + 1]]:
            x -= rti[s[i]]
        else:
            x += rti[s[i]]
    return x


print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
