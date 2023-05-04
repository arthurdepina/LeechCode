def isPalindrome(x):
    x = str(x)
    for i in range(len(x)):
        if x[i] == x[len(x) - i - 1]:
            continue
        else:
            return False
    return True


torf = isPalindrome(1234554321)
print(torf)
