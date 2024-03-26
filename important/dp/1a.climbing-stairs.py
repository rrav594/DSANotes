class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        def helper(n):
            if n == 0 or n == 1: 
                return 1
            if n < 0:
                return 0
            if dp[n] != -1:
                return dp[n]
            dp[n] = helper(n-1)+helper(n-2)
            return dp[n]
        return helper(n)
    
    
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
    
    
class Solution:
    def climbStairs(self, n: int) -> int:
        prev, prev2 = 1, 1
        curr = 0
        for i in range(2, n+1):
            curr = prev+prev2
            prev2, prev = prev, curr
        return prev
            