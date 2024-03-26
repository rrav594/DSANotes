class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1 for i in range(amount+1)]for i in range(n)]
        def helper(n, amount):
            if dp[n][amount] != -1:
                return dp[n][amount]
            if n == 0:
                if amount%coins[n] == 0:
                    return amount//coins[n]
                else:
                    return float("inf")
            pick = float("inf")
            if coins[n] <= amount:
                pick = helper(n, amount-coins[n])+1
            notPick = helper(n-1, amount)
            dp[n][amount] = min(pick, notPick)
            return dp[n][amount]
        ans = helper(n-1, amount)
        return -1 if ans == float("inf") else ans



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[0 for i in range(amount+1)]for i in range(n)]
        for i in range(amount+1):
            if i % coins[0] == 0:
                dp[0][i] = i//coins[0]
            else:
                dp[0][i] = float("inf")
        for i in range(1, n):
            for j in range(amount+1):
                pick = float("inf")
                if coins[i] <= j:
                    pick = 1+dp[i][j-coins[i]]
                notPick = dp[i-1][j]
                dp[i][j] = min(pick, notPick)
        if dp[n-1][amount] == float("inf"):
            return -1
        return dp[n-1][amount]