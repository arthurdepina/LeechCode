# 36. Valid Sudoku


def isValidSudoku(board: list[list[str]]) -> bool:
    for i in range(9):
        for j in range(9):
            current = board[i][j]

            if current == ".": continue

            # searching the line:
            for m in range(9):
                if m != j and board[i][m] == current: return False

            # searching the column:
            for n in range(9):
                if n != i and board[n][j] == current: return False
            
            # searching the 3x3 square:
            for p in range((i//3) * 3, ((i//3) * 3) + 3):
                for q in range((j//3) * 3, ((j//3) * 3) + 3):
                    if p != i or q != j:
                        if board[p][q] == current: return False
    
    return True




print(isValidSudoku([["5","3",".",".","7",".",".",".","."],
                     ["6",".",".","1","9","5",".",".","."],
                     [".","9","8",".",".",".",".","6","."],
                     ["8",".",".",".","6",".",".",".","3"],
                     ["4",".",".","8",".","3",".",".","1"],
                     ["7",".",".",".","2",".",".",".","6"],
                     [".","6",".",".",".",".","2","8","."],
                     [".",".",".","4","1","9",".",".","5"],
                     [".",".",".",".","8",".",".","7","9"]])) # True

print(isValidSudoku([["8","3",".",".","7",".",".",".","."],
                     ["6",".",".","1","9","5",".",".","."],
                     [".","9","8",".",".",".",".","6","."],
                     ["8",".",".",".","6",".",".",".","3"],
                     ["4",".",".","8",".","3",".",".","1"],
                     ["7",".",".",".","2",".",".",".","6"],
                     [".","6",".",".",".",".","2","8","."],
                     [".",".",".","4","1","9",".",".","5"],
                     [".",".",".",".","8",".",".","7","9"]])) # False
