# 931. Minimum Falling Path Sum

def minFallingPathSum(matrix) -> int:
    max_depth = len(matrix)
    print(max_depth)
    smallest_for_i = [999999] * max_depth
    initial_i = 0

    def min_path(matrix, current_path, smallest_for_i, i, depth, initial_i):
        print("depth = ", depth)
        if depth == max_depth:
            if current_path < smallest_for_i[initial_i]:
                smallest_for_i[initial_i] = current_path
                print("smallest_for_i = ", smallest_for_i)
            return

        current_path += matrix[depth][i]
        print("current_path = ", current_path)
        min_width = i - 1 if i > 0 else 0
        max_width = i + 1 if i < max_depth - 1 else max_depth - 1
        print("min_width = ", min_width)
        print("max_width = ", max_width)

        for i in range(min_width, max_width + 1):
            print("i = ", i)
            min_path(matrix, current_path, smallest_for_i, i, depth + 1, initial_i)
    
    for initial_i in range(max_depth):
        print("***********************")
        print("initial_i = ", initial_i)
        print("***********************")
        min_path(matrix, 0, smallest_for_i, initial_i, 0, initial_i)
    
    return smallest_for_i


print(minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])) # 13
print(minFallingPathSum([[-19,57],[-40,-5]]))       # -59
