def isPalindrome(s: str) -> bool:
    s = ''.join(i for i in s if i.isalnum()).lower()
    if s[::-1] == s: return True
    return False


print(isPalindrome("A man, a plan, a canal: Panama"))   # True
print(isPalindrome("race a car"))                       # False
print(isPalindrome(" "))                                # True          
