# 66. Plus One

def plusOne(digits) -> list[int]:
    digits[-1] += 1
    if digits[-1] < 10: return digits

    counter = len(digits) - 1 
    while digits[counter] >= 10:
        if counter > 0:
            digits[counter - 1] += 1
            digits[counter] -= 10
            counter -= 1
        else:
            digits.insert(0, 1)
            digits[counter + 1] -= 10
            break
    
    return digits


print(plusOne([1,2,3]))     # [1,2,4]
print(plusOne([4,3,2,1]))   # [4,3,2,2]
print(plusOne([9]))         # [1,0]


# I thought this solution below would've been
# better, but apparently my original solution
# is faster, at least according to leetcode's
# clock, which I wouldn't say is very reliable.
# Either way, I'm leaving this solution down
# here because it's elegant, at least to my
# standards.

def plusOne_2(self, digits) -> int:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    digits.insert(0, 1)
    return digits
    
# the original idea comes from here:
# https://leetcode.com/problems/plus-one/solutions/2706861/java-fastest-0ms-runtime-easy-and-elegant-solution/