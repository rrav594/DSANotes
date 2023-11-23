# 1) DP
# Bottom-up
dp = [-1]*(10000000)
class Solution:
    def countFriendsPairings(self, n):
        # code here 
        def helper(n):    
            global dp
            if dp[n] != -1:
                return dp[n]
            if n > 2:
                dp[n] = self.countFriendsPairings(n-1) + (n-1)*self.countFriendsPairings(n-2)
                return dp[n]
            else:
                dp[n] = n
                return dp[n]
        helper(n)
        return dp[n] % (10**9+7)

# Top-Down
class Solution:
    def countFriendsPairings(self, n):
        # code here 
        dp = [0 for i in range(n+1)]
        for i in range(n+1):
            if i <= 2:
                dp[i] = i
            else:
                dp[i] = dp[i-1] + (i-1) * dp[i-2]
        return dp[n]


# 2) Iterative
class Solution:
    def countFriendsPairings(self, n):
        # code here
        a, b, c = 1, 2, 0;
        if (n <= 2):
            return n;
        for i in range(3, n + 1):
            c = b + (i - 1) * a;
            a = b;
            b = c;
        return c % (10**9 + 7)