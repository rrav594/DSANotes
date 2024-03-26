class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[-1 for i in range(col)]for i in range(row)]
        def helper(m, n):
            if grid[m][n] == 1 or m < 0 or n < 0:
                return 0
            if m == 0 and n == 0:
                return 1
            if dp[m][n] != -1:
                return dp[m][n]
            dp[m][n] = helper(m-1, n)+helper(m, n-1)
            return dp[m][n]
        return helper(row-1, col-1)
        