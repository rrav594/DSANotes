class Solution:
    def findPath(self, m, n):
        def helper(i, j, m, n, ans, curr):
            if i<0 or j<0 or i>=n or j>=n or m[i][j]==0:
                return 0
            if i == n-1 and j == n-1:
                ans.append(curr)
            m[i][j] = 0
            c1 = helper(i+1, j, m, n, ans, curr+"D")
            c1 = helper(i, j+1, m, n, ans, curr+"R")
            c1 = helper(i-1, j, m, n, ans, curr+"U")
            c1 = helper(i, j-1, m, n, ans, curr+"L")
            m[i][j] = 1
        ans = []
        curr = ""
        helper(0, 0, m, n, ans, curr)
        return ans
        
        