# 67. Add Binary

def addBinary(a: str, b : str) -> str:
    i_a   = len(a) - 1
    i_b   = len(b) - 1
    carry = False
    total = ""
    while i_a >= 0 and i_b >= 0:
        if a[i_a] == "1" and b[i_b] == "1":
            if not carry:
                total = "0" + total
            else:
                total = "1" + total
            carry = True
        elif (a[i_a] == "1") ^ (b[i_b] == "1"):
            if not carry:
                total = "1" + total
            else:
                total = "0" + total
                carry = True
        else:
            if not carry:
                total = "0" + total
            else:
                total = "1" + total
                carry = False
        i_a -= 1
        i_b -= 1

    total = a[:i_a + 1] + b[:i_b + 1] + total

    if carry:
        i_g = i_a + i_b + 1
        while i_g >= 0 and carry:
            if total[i_g] == '0':
                total = total[:i_g] + '1' + total[i_g + 1:]
                carry = False
            else:
                total = total[:i_g] + '0' + total[i_g + 1:]
            i_g -= 1
            
        if carry: total = '1' + total
    
    return total


print(addBinary("11", "1"))             # "100"
print(addBinary("1010", "1011"))        # "10101"
print(addBinary('1111110', '11100'))    # "10011010"
