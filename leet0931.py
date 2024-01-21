# 931. Minimum Falling Path Sum

def minFallingPathSum(matrix) -> int:
    N = len(matrix) # dimensions of the matrix
    cache = dict()

    def depth_first_search(row, column):
        if row == N: return 0
        if column == -1 or column == N: return float('inf')

        if (row, column) in cache: return cache[(row, column)]

        min_path = matrix[row][column] + min(depth_first_search(row + 1, column + 1),
                                             depth_first_search(row + 1, column),
                                             depth_first_search(row + 1, column - 1)
                                             )
        
        cache[(row, column)] = min_path

        return min_path
        
    
    min_path = float('inf') # the result we're trying to minimize
    for column in range(N): # iterating through the first row
        min_path = min(min_path, depth_first_search(0, column))

    return min_path


print(minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])) # 13
print(minFallingPathSum([[-19,57],[-40,-5]]))       # -59


# This solution works fine (still fairly slow)
# but I'm not sure how I would've come up with it
# by myself. This solution comes from neetcode:
# https://youtu.be/b_F3mz9l-uQ?si=EK5wbkxm_q6slviQ
