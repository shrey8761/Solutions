class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for row in range(1,len(matrix)):
            for col in range(len(matrix)):
                temp = matrix[row-1][col]
                if col-1 >= 0:
                    temp = min(temp,matrix[row-1][col-1])
                if col+1 < len(matrix):
                    temp = min(temp,matrix[row-1][col+1])
                matrix[row][col] += temp
        return min(matrix[-1])