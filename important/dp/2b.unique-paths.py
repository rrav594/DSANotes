class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n)]for i in range(m)]
        def helper(m, n):
            if dp[m][n] != -1:
                return dp[m][n]
            if m == 0 or n == 0:
                dp[m][n] = 1
                return dp[m][n]
            if m < 0 or n < 0:
                return 0
            dp[m][n] = helper(m-1, n)+helper(m, n-1)
            return dp[m][n]
        return helper(m-1, n-1)
        


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)]for i in range(m)]
        for i in range(m):
            for j in  range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
    

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1 for i in range(n)]
        for i in range(1, m):
            curr = [0 for i in range(n)]
            for j in range(n):
                curr[j] = curr[j-1]+prev[j] if j > 0 else prev[j]
            prev = curr
        return prev[-1]