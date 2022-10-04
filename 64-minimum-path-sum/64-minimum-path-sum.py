class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = [[-1 for i in range(len(grid[0]))] for i in range(len(grid))]

        def find_sum(grid: List[List[int]], memo: List[List[int]], row: int, col: int) -> int:
            row_max = len(grid)
            col_max = len(grid[0])

            if row >= row_max or col >= col_max:
                return 0xFFFF

            if row == row_max - 1 and col == col_max - 1:
                return grid[row][col]

            if memo[row][col] != -1:
                return memo[row][col]

            memo[row][col] = grid[row][col] + min(find_sum(grid, memo, row, col + 1), find_sum(grid, memo, row + 1, col))

            return memo[row][col]

        return find_sum(grid, memo, 0, 0)
