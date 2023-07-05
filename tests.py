class Solution(object):
    def isValid(self, s):
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
                            return False
                        else:
                            break
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
                else:
                    local_open_square = local_close_square = local_open_curly = local_close_curly = 0
            elif s[i] == "[":
                open_square += 1
                local_open_parenthesis = 0
                local_open_curly = 0
                local_close_parenthesis = 0
                local_close_curly = 0
                for j in range(i, len(s)):
                    if s[j] == "]":
                        if (j + 1 - i) % 2 != 0:
                            return False
                        else:
                            break
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
                else:
                    local_open_parenthesis = local_close_parenthesis = local_open_curly = local_close_curly = 0
            elif s[i] == "{":
                open_curly += 1
                local_open_parenthesis = 0
                local_open_square = 0
                local_close_parenthesis = 0
                local_close_square = 0
                for j in range(i, len(s)):
                    if s[j] == "}":
                        if (j + 1 - i) % 2 != 0:
                            return False
                        else:
                            break
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
                else:
                    local_open_parenthesis = local_close_parenthesis = local_open_square = local_close_square = 0
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
