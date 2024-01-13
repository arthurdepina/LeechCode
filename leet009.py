# 09. Palindrome Number

def isPalindrome(x) -> bool:
    if x < 0 or x % 10 == 0: return False
    backwards = 0
    while x > backwards:
        backwards = backwards * 10 + x % 10
        x //= 10
    return (x == backwards or x == backwards//10)


torf = isPalindrome(1221)
print(torf)


# def isPalindrome(x):
#     x = str(x)
#     for i in range(len(x)):
#         if x[i] == x[len(x) - i - 1]:
#             continue
#         else:
#             return False
#     return True
