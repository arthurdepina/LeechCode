# 66. Plus One

def plusOne(digits) -> int:
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
