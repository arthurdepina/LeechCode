class Solution(object):
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        output = [[1], [1, 1]]
        for i in range(2, numRows):
            current = []
            previous = output[i - 1]
            for j in range(len(previous) + 1):
                if j == 0:
                    current.append(1)
                elif j == len(previous):
                    current.append(1)
                else:
                    current.append(previous[j - 1] + previous[j])
            output.append(current)
        return output
