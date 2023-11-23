# 1) DP Solution O(n) Space

class Solution:
    def countWays(self,n,k):
        #code here.
        dp = [0] *(n+1)
        mod = 10**9+7
        if n == 1:
            return k
        dp[1] = k
        dp[2] = k*k
        for i in range(3, n+1):
            dp[i] = ((k-1)*(dp[i-1]+dp[i-2])) % mod
        return dp[n]
   

# 2) Constant Space
class Solution:
    def countWays(self,n,k):
        #code here.
        mod = 10**9 + 7
        if n == 1:
            return k
        same, diff = 0, k
        total = same+diff
        for i in range(2, n+1):
            same = diff
            diff = total * (k-1)
            diff = diff % mod
            total = (same+diff)%mod
        return total
