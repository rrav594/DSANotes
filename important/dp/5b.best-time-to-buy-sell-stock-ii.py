class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit
        

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[-1 for i in range(2)]for i in range(n)]
        def getAns(i, action):
            if i == n:
                return 0
            if dp[i][action] != -1:
                return dp[i][action]
            profit = 0
            if action == 0: #buy
                profit = max(0+getAns(i+1, 0), -prices[i]+getAns(i+1, 1))
            elif action == 1: #sell
                profit = max(0+getAns(i+1, 1), prices[i]+getAns(i+1, 0))
            dp[i][action] = profit
            return dp[i][action]
        ans = getAns(0, 0)  # Start with buying (0) at the first day (0)
        return ans
        

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1 for i in range(2)]for i in range(n+1)]
        dp[n][0] = dp[n][1] = 0
        for i in range(n-1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy == 0:
                    profit = max(0+dp[i+1][0], -prices[i]+dp[i+1][1])
                elif buy == 1:
                    profit = max(0+dp[i+1][1], prices[i]+dp[i+1][0])
                dp[i][buy] = profit
        return dp[0][0]