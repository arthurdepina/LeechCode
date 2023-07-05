"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
"""
list_of_symbols = []


def isValid(s):
    pass


print(isValid("()"), "---- should be TRUE")       # Should print "true"
print(isValid("()[]{}"), "---- should be TRUE")   # Should print "true"
print(isValid("(]"), "-- should be FALSE")      # Should print "false"
print(isValid("([)]"), "-- should be FALSE")    # Should print "false"
print(isValid("{[]}"), "---- should be TRUE")     # Should print "true"
print(isValid("[()]"), "---- should be TRUE")     # Should print "true"
print(isValid("(("), "-- should be FALSE")      # Should print "false"
print(isValid("(){}}{"), "-- should be FALSE")  # Should print "false"


# Pensei em uma solução alternativa, para cada ( [ ou {, verifique se entre a abertura e
# o fechamento existe um número par de itens. Não sei como ficaria o tempo de execução
# disso, mas tanto faz.
