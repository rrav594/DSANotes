class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1 for i in range(k+1)]for i in range(2)]for i in range(n)]
        def getAns(i, action, cap):
            if i == n or cap == 0:
                return 0
            profit = 0
            if dp[i][action][cap] != -1:
                return dp[i][action][cap]
            if action == 0:
                profit = max(0+getAns(i+1, 0, cap), -prices[i]+getAns(i+1, 1, cap))
            else:
                profit = max(0+getAns(i+1, 1, cap), prices[i]+getAns(i+1, 0, cap-1))
            dp[i][action][cap] = profit
            return profit
        return getAns(0, 0, k)