# 020. Valid Parenthesis

def isValid(s):
    pseudo_stack = list()
    for i in s:
        if i == "(" or i == "[" or i == "{":
            pseudo_stack.append(i)
        if i in ")]}":
            if not pseudo_stack or \
                i == ")" and "(" not in pseudo_stack or \
                i == "]" and "[" not in pseudo_stack or \
                i == "}" and "{" not in pseudo_stack:
                return False
            if i == ")" and pseudo_stack[-1] == "(": pseudo_stack.pop()
            if i == "]" and pseudo_stack[-1] == "[": pseudo_stack.pop()
            if i == "}" and pseudo_stack[-1] == "{": pseudo_stack.pop()
    return not pseudo_stack


print(isValid("[][{[{{}}[][]{{}}]}]"))
