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
            local_open_square = 0
            local_open_curly = 0
            local_close_square = 0
            local_close_curly = 0
            for j in range(i, len(s)):
                if s[j] == ")":
                    if (j + 1 - i) % 2 != 0:
                        continue
                    else:
                        if local_open_square == local_close_square and local_close_curly == local_close_curly:
                            local_open_square = local_close_square = local_open_curly = local_close_curly = 0
                            break
                        else:
                            continue
                if s[j] == "[":
                    local_open_square += 1
                if s[j] == "{":
                    local_open_curly += 1
                if s[j] == "]":
                    local_close_square += 1
                if s[j] == "}":
                    local_close_curly += 1
                if j == len(s) - 1:
                    return False
            if local_open_square != local_close_square:
                return False
            if local_open_curly != local_close_curly:
                return False
        elif s[i] == "[":
            open_square += 1
            local_open_parenthesis = 0
            local_open_curly = 0
            local_close_parenthesis = 0
            local_close_curly = 0
            for j in range(i, len(s)):
                if s[j] == "]":
                    if (j + 1 - i) % 2 != 0:
                        continue
                    else:
                        if local_open_parenthesis == local_close_parenthesis and local_open_curly == local_close_curly:
                            local_open_parenthesis = local_close_parenthesis = local_open_curly = local_close_curly = 0
                            break
                        else:
                            continue
                if s[j] == "(":
                    local_open_parenthesis += 1
                if s[j] == "{":
                    local_open_curly += 1
                if s[j] == ")":
                    local_close_parenthesis += 1
                if s[j] == "}":
                    local_close_curly += 1
                if j == len(s) - 1:
                    return False
            if local_open_parenthesis != local_close_parenthesis:
                return False
            if local_open_curly != local_close_curly:
                return False
        elif s[i] == "{":
            open_curly += 1
            local_open_parenthesis = 0
            local_open_square = 0
            local_close_parenthesis = 0
            local_close_square = 0
            for j in range(i, len(s)):
                if s[j] == "}":
                    if (j + 1 - i) % 2 != 0:
                        continue
                    else:
                        if local_open_parenthesis == local_close_parenthesis and local_open_square == local_close_square:
                            local_open_parenthesis = local_close_parenthesis = local_open_square = local_close_square = 0
                            break
                        else:
                            continue
                if s[j] == "(":
                    local_open_parenthesis += 1
                if s[j] == "[":
                    local_open_square += 1
                if s[j] == ")":
                    local_close_parenthesis += 1
                if s[j] == "]":
                    local_close_square += 1
                if j == len(s) - 1:
                    return False
            if local_open_parenthesis != local_close_parenthesis:
                return False
            if local_open_square != local_close_square:
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
print(isValid("({[}])"), "-- should be False")
print(isValid("[({])}"), "-- should be False")
print(isValid("({[)}]"), "-- should be False")
print(isValid("(([]){})"), "---- should be True")
print(isValid("[({(())}[()])]"), "---- should be True")
print(isValid("[][{[{{}}[][]{{}}]}]"), "---- should be True")


# That was an absolutely retarded solution.
# There is, with 100% certainty, an easy way to do this.
# BUT I missed the Palindromes class at uni
# and I REFUSE to look up anything while solving these problems.
# This was truly awful. Fuck. It's 3:39 AM. I wanna go to sleep.

# ...

# BUT FIRST! Let's look at the actual proper solution to this problem
# ...
# As I thought, you use a Stack.
# Reading through the string, if it's an opening symbol, you append it to
# the stack. Otherwise you compare it with the last item in the stack [-1],
# if they are pairs, you remove it from the stack, else you return False.
# yo yo! If the stack is empty by the time you finsh going through the string
# you can return True! yeah!!!! so cool!!!! I'm so tired, I wanna go to sleep.
