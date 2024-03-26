class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1 for i in range(amount+1)]for i in range(n)]
        def helper(n, amount):
            if dp[n][amount] != -1:
                return dp[n][amount]
            if n == 0:
                if amount % coins[n] == 0:
                    return 1
                return 0
            pick = 0
            if coins[n] <= amount:
                pick = helper(n, amount-coins[n])
            notPick = helper(n-1, amount)
            dp[n][amount] = pick+notPick
            return dp[n][amount]
        return helper(n-1, amount)
    


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for i in range(amount+1)]for i in range(n)]
        for i in range(amount+1):
            if i%coins[0] == 0:
                dp[0][i] = 1
            else:
                dp[0][i] = 0
        for i in range(1, n):
            for j in range(amount+1):
                pick = 0
                if coins[i] <= j:
                    pick = dp[i][j-coins[i]]
                notPick = dp[i-1][j]
                dp[i][j] = pick+notPick
        return dp[n-1][amount]