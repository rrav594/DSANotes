# 1) Recursive
class Solution:
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        if x == 0 or y == 0:
            return 0
        elif s1[x-1] == s2[y-1]:
            return 1+self.lcs(x-1, y-1, s1, s2)
        else:
            return max(self.lcs(x-1, y, s1, s2), self.lcs(x, y-1, s1, s2))

# 2) Memoization(Top-Down)
class Solution:   
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        def helper(x, y, s1, s2, dp):
            if x == 0 or y == 0:
                return 0
            if dp[x][y] != -1:
                return dp[x][y]
            if s1[x-1] == s2[y-1]:
                dp[x][y] = 1 + helper(x-1, y-1, s1, s2, dp)
                return dp[x][y]
            dp[x][y] = max(helper(x-1, y, s1, s2, dp), helper(x, y-1, s1, s2, dp))
            return dp[x][y]
        dp = [[-1 for i in range(y+1)]for i in range(x+1)]
        helper(x, y, s1, s2, dp)
        return dp[x][y]
 
# 3) Tabulation(Bottom-Up)
class Solution:
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        dp = [[-1 for i in range(y+1)]for i in range(x+1)]
        for i in range(x+1):
            for j in range(y+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[x][y]