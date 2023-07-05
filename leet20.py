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
    expects_closing = []

    for character in s:
        # The openings
        if character == "(":
            expects_closing.append("parenthesis")
            open_parenthesis = True
        elif character == "[":
            expects_closing.append("square brackets")
            open_square_brackets = True
        elif character == "{":
            expects_closing.append("curly brackets")
            open_curly_brackets = True
        # The closings
        elif character == ")":
            if not open_parenthesis:
                return False
            if close_square_brackets and expects_closing.index("square brackets") < expects_closing.index("parenthesis"):
                return False
            if close_curly_brackets and expects_closing.index("curly brackets") < expects_closing.index("parenthesis"):
                return False
            close_parenthesis = True
        elif character == "]":
            if not open_square_brackets:
                return False
            if close_parenthesis and expects_closing.index("parenthesis") < expects_closing.index("square brackets"):
                return False
            if close_curly_brackets and expects_closing.index("curly brackets") < expects_closing.index("square brackets"):
                return False
            close_square_brackets = True
        elif character == "}":
            if not open_curly_brackets:
                return False
            if close_parenthesis and expects_closing.index("parenthesis") < expects_closing.index("curly brackets"):
                return False
            if close_square_brackets and expects_closing.index("square brackets") < expects_closing.index("curly brackets"):
                return False
            close_curly_brackets = True
    return True


print(isValid("()"), "-- should be TRUE")      # Should print "true"
print(isValid("()[]{}"), "-- should be TRUE")  # Should print "true"
print(isValid("(]"), "-- should be FALSE")     # Should print "false"
print(isValid("([)]"), "-- should be FALSE")    # Should print "false"
print(isValid("{[]}"), "-- should be TRUE")    # Should print "true"
print(isValid("[()]"), "-- should be TRUE")    # Should print "true"


# Pensei em uma solução alternativa, para cada ( [ ou {, verifique se entre a abertura e
# o fechamento existe um número par de itens. Não sei como ficaria o tempo de execução
# disso, mas tanto faz.
