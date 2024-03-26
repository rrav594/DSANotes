class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[-1 for i in range(col)]for i in range(row)]
        def helper(m, n):
            if n < 0 or n >= col:
                return float("inf")
            if m == 0:
                return matrix[m][n]
            if dp[m][n] != -1:
                return dp[m][n]
            dp[m][n] = matrix[m][n]+min(helper(m-1, n-1), helper(m-1, n), helper(m-1, n+1))
            return dp[m][n]
        ans = float("inf")
        for i in range(col):
            res = helper(row-1, i)
            ans = min(ans, res)
        return ans
    


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for i in range(col)]for i in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0:
                    dp[i][j] = matrix[i][j]
                    continue
                left, up, right = float("inf"), float("inf"), float("inf")
                if j-1 >= 0:
                    left = dp[i-1][j-1]
                up = dp[i-1][j]
                if j+1 < col:
                    right = dp[i-1][j+1]
                dp[i][j] = matrix[i][j]+min(left, up, right)
        return min(dp[row-1])            
    


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        prev = [0 for i in range(col)]
        for i in range(col):
            prev[i] = matrix[0][i]
        for i in range(1, row):
            curr = [0 for k in range(col)]
            for j in range(col):
                left = right = up = float("inf")
                curr[j] = matrix[i][j]
                if j-1 >= 0:
                    left = prev[j-1]
                if j+1 < col:
                    right = prev[j+1]
                up = prev[j]
                curr[j] += min(right, left, up)
            prev = curr
        return min(prev)