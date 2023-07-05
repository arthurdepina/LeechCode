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
    expected_closing = []

    for character in s:
        # The openings
        if character == "(":
            expected_closing.append("parenthesis")
            open_parenthesis = True
        elif character == "[":
            expected_closing.append("square brackets")
            open_square_brackets = True
        elif character == "{":
            expected_closing.append("curly brackets")
            open_curly_brackets = True
        # The closings
        elif character == ")":
            if not open_parenthesis:
                return False
            if 


print(isValid("()"))      # Should print "true"
print(isValid("()[]{}"))  # Should print "true"
print(isValid("(]"))      # Should print "false"
print(isValid("([)]"))    # Should print "false"
print(isValid("{[]}"))    # Should print "true"
