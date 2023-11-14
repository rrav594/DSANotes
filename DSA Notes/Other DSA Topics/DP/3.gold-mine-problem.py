# 1) Recursion
class Solution:
    def maxGold(self, n, m, M):
        # code here
        def collectGold(M, x, y, n, m):
            if x<0 or x==n or y==m:
                return 0
            rightUpper = collectGold(M, x-1, y+1, n, m)
            right = collectGold(M, x, y+1, n, m)
            rightLower = collectGold(M, x+1, y+1, n, m)
            return M[x][y] + max(rightUpper, right, rightLower)
        maxGold = 0
        for i in range(n):
            goldCollected = collectGold(M, i, 0, n, m)
            maxGold = max(maxGold, goldCollected)
        return maxGold
    
# 2) DP 
# Memoization/ Bottom-up approrach
class Solution:
    def maxGold(self, n, m, M):
        # code here
        def collectGold(M, x, y, n, m, dp):
            if x<0 or x==n or y==m:
                return 0
            if dp[x][y] != -1:
                return dp[x][y]
            rightUpper = collectGold(M, x-1, y+1, n, m, dp)
            right = collectGold(M, x, y+1, n, m, dp)
            rightLower = collectGold(M, x+1, y+1, n, m, dp)
            dp[x][y] =  M[x][y] + max(rightUpper, right, rightLower)
            return dp[x][y]
        dp = [[-1 for i in range(m)]for i in range(n)]
        maxGold = 0
        for i in range(n):
            goldCollected = collectGold(M, i, 0, n, m, dp)
            maxGold = max(maxGold, goldCollected)
        return maxGold
    
# Top-Down
class Solution:
    def maxGold(self, n, m, M):
        # code here
        dp = [[0 for i in range(m)]for i in range(n)]
        for col in range(m-1, -1,-1):
            for row in range(n):
                if col == m-1:
                    right = 0
                else:
                    right = dp[row][col+1]
                if row == 0 or col == m-1:
                    rightUpper = 0
                else:
                    rightUpper = dp[row-1][col+1]
                if row == n-1 or col == m-1:
                    rightLower = 0
                else:
                    rightLower = dp[row+1][col+1]
                dp[row][col] = M[row][col] + max(right, rightUpper, rightLower)
        res = dp[0][0]
        for i in range(1, n):
            res = max(res, dp[i][0])
        return res