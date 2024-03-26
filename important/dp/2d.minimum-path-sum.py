class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[-1 for i in range(col)]for j in range(row)]
        def helper(m, n):
            if m == 0 and n == 0:
                return grid[m][n]
            if m < 0 or n < 0:
                return float("inf")
            if dp[m][n] != -1:
                return dp[m][n]
            dp[m][n] = grid[m][n]+min(helper(m-1, n), helper(m, n-1))
            return dp[m][n]
        return helper(row-1, col-1)
    

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[-1 for i in range(col)]for j in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                    continue
                dp[i][j] = grid[i][j]+min(dp[i-1][j] if dp[i-1][j] != -1 else float("inf"), dp[i][j-1] if dp[i][j-1] != -1 else float("inf"))
        return dp[row-1][col-1]
    

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        prev = [0 for i in range(col)]
        for i in range(col):
            if i == 0:
                prev[i] = grid[0][0]
            else:
                prev[i] = grid[0][i]+prev[i-1]
        for i in range(1, row):
            curr = [0 for i in range(col)]
            for j in range(col):
                if j == 0:
                    curr[j] = grid[i][j]+prev[j]
                else:
                    curr[j] = grid[i][j]+min(curr[j-1], prev[j])
            prev = curr
        return prev[-1]
                