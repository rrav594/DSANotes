# 1) Brute-Force(Recursion)
class Solution:
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        if n == 0:
            return 0
        if n < 0:
            return float("-inf")
        a = self.maximizeTheCuts(n-x, x, y, z) + 1
        b = self.maximizeTheCuts(n-y, x, y, z) + 1
        c = self.maximizeTheCuts(n-z, x, y, z) + 1
        
        d = max(a, b, c)
        return d
        
    
# 2) Memoization (Top-Down)
class Solution:
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        def maxCuts(n, x, y, z, dp):
            if n == 0:
                return 0
            if dp[n] != -1:
                return dp[n]
            a, b, c = float("-inf"), float("-inf"), float("-inf")
            if x <= n:
                a = maxCuts(n-x, x, y, z, dp)
            if y <= n:
                b = maxCuts(n-y, x, y, z, dp)
            if z <= n:
                c = maxCuts(n-z, x, y, z, dp)
            dp[n] = 1 + max(a, b, c)
            return dp[n]
        dp = [-1] * (100000)
        maxCuts(n, x, y, z, dp)
        return 0 if dp[n] < 0 else dp[n]

# 3) Tabulation (Bottom-up)
class Solution:
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        dp = [-1] * (n+1)
        dp[0] = 0
        for i in range(n+1):
            if dp[i] == -1:
                continue
            if i+x <= n:
                dp[i+x] = max(dp[i+x], dp[i]+1)
            if i+y <= n:
                dp[i+y] = max(dp[i+y], dp[i]+1)
            if i+z <= n:
                dp[i+z] = max(dp[i+z], dp[i]+1)
        if dp[n] == -1:
            return 0
        return dp[n]
     
        