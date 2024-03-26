class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp = [[-1 for i in range(W+1)]for i in range(n)]
        def helper(n, w):
            if dp[n][w] != -1:
                return dp[n][w]
            if n == 0:
                return val[n] if wt[n] <= w else 0
            notPick = helper(n-1, w)
            pick = float("-inf")
            if wt[n] <= w:
                pick = val[n] + helper(n-1, w-wt[n])
            dp[n][w] = max(pick, notPick)
            return dp[n][w]
        return helper(n-1, W)
    

    class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp = [[0 for i in range(W+1)]for i in range(n)]
        for i in range(n):
            for j in range(W+1):
                if i == 0 and wt[i] <= j:
                    dp[i][j] = val[i]
                    continue
                notPick = dp[i-1][j]
                pick = float("-inf")
                if wt[i] <= j:
                    pick = val[i]+dp[i-1][j-wt[i]]
                dp[i][j] = max(pick, notPick)
        return dp[n-1][W]
    

class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        prev = [0 for i in range(W+1)]
        for i in range(W+1):
            if wt[0] <= i:
                prev[i] = val[0]
        for i in range(1, n):
            curr = [0 for i in range(W+1)]
            for j in range(W+1):
                notPick = prev[j]
                pick = float("-inf")
                if wt[i] <= j:
                    pick = val[i]+prev[j-wt[i]]
                curr[j] = max(pick, notPick)
            prev = curr
        return prev[-1]