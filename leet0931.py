# 931. Minimum Falling Path Sum

def minFallingPathSum(matrix) -> int:
    N = len(matrix) # dimensions of the matrix
    
    for row in range(1, N):
        for column in range(N):
            up    = matrix[row - 1][column]
            left  = matrix[row - 1][column - 1] if column != 0     else float('inf')
            right = matrix[row - 1][column + 1] if column != N - 1 else float('inf')
            matrix[row][column] += min(up, left, right)
    
    return min(matrix[-1])

print(minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])) # 13
print(minFallingPathSum([[-19,57],[-40,-5]]))       # -59


# This is a much nicer solution than the previous one
# and I also can understand it better. Again, credits
# to neetcode: youtu.be/b_F3mz9l-uQ?si=EK5wbkxm_q6slviQ
