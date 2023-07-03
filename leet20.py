"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
"""


def isValid(s):
    open_parenthesis = False
    open_square_brackets = False
    open_curly_brackets = False
    close_parenthesis = False
    close_square_brackets = False
    close_curly_brackets = False

    for character in s:
        if character == "(":  # THE OPENINGS
            if close_parenthesis:
                return "false"
            open_parenthesis = True
        elif character == "[":
            if close_square_brackets:
                return "false"
            open_square_brackets = True
        elif character == "{":
            if close_curly_brackets:
                return "false"
            open_curly_brackets = True
        elif character == ")":  # THE CLOSINGS
            if not open_parenthesis:
                return "false"
            if open_square_brackets and not close_square_brackets:
                return "false"
            if open_curly_brackets and not close_curly_brackets:
                return "false"
            close_parenthesis = True
        elif character == "]":
            if not open_square_brackets:
                return "false"
            if open_parenthesis and not close_parenthesis:
                return "false"
            if open_curly_brackets and not close_curly_brackets:
                return "false"
            close_square_brackets = True
        elif character == "}":
            if not open_curly_brackets:
                return "false"
            if open_parenthesis and not close_parenthesis:
                return "false"
            if open_square_brackets and not close_square_brackets:
                return "false"
            close_curly_brackets = True

    return "true"


print(isValid("()"))      # Should print "true"
print(isValid("()[]{}"))  # Should print "true"
print(isValid("(]"))      # Should print "false"
print(isValid("([)]"))    # Should print "false"
print(isValid("{[]}"))    # Should print "true"
