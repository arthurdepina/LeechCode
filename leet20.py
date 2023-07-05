"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
"""


def isValid(s):
    open_parenthesis = 0
    open_square = 0
    open_curly = 0
    close_parenthesis = 0
    close_square = 0
    close_curly = 0
    for i in range(len(s)):
        if s[i] == "(":
            open_parenthesis += 1
            for j in range(i, len(s)):
                if s[j] == ")":
                    if (j + 1 - i) % 2 != 0:
                        return False
                    else:
                        break
                if j == len(s) - 1:
                    return False
        elif s[i] == "[":
            open_square += 1
            for j in range(i, len(s)):
                if s[j] == "]":
                    if (j + 1 - i) % 2 != 0:
                        return False
                    else:
                        break
                if j == len(s) - 1:
                    return False
        elif s[i] == "{":
            open_curly += 1
            for j in range(i, len(s)):
                if s[j] == "}":
                    if (j + 1 - i) % 2 != 0:
                        return False
                    else:
                        break
                if j == len(s) - 1:
                    return False
        elif s[i] == ")":
            close_parenthesis += 1
        elif s[i] == "]":
            close_square += 1
        elif s[i] == "}":
            close_curly += 1
    if open_parenthesis != close_parenthesis:
        return False
    if open_square != close_square:
        return False
    if open_curly != close_curly:
        return False
    return True


print(isValid("()"), "---- should be TRUE")      # Should print "true"
print(isValid("()[]{}"), "---- should be TRUE")  # Should print "true"
print(isValid("(]"), "-- should be FALSE")       # Should print "false"
print(isValid("([)]"), "-- should be FALSE")     # Should print "false"
print(isValid("{[]}"), "---- should be TRUE")    # Should print "true"
print(isValid("[()]"), "---- should be TRUE")    # Should print "true"
print(isValid("(("), "-- should be False")       # Should print "false"
print(isValid("(){}}{"), "-- should be False")   # Should print "false"
print(isValid("[[[]"), "-- should be False")
print(isValid("([}}])"), "-- should be False")
print(isValid("[({])}"), "-- should be False")


# Pensei em uma solução alternativa, para cada ( [ ou {, verifique se entre a abertura e
# o fechamento existe um número par de itens. Não sei como ficaria o tempo de execução
# disso, mas tanto faz.
