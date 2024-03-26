class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = [0]*n
        max_ = prices[n-1]
        for i in range(n-2, -1, -1):
            if prices[i] > max_:
                max_ = prices[i]
            profit[i] = max(profit[i+1], max_-prices[i])
        min_ = prices[0]
        for i in range(1, n):
            if prices[i] < min_:
                min_ = prices[i]
            profit[i] = max(profit[i-1], profit[i]+prices[i]-min_)
        return profit[n-1]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1 for i in range(3)]for i in range(2)]for i in range(n)]
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
        return getAns(0, 0, 2)  # Start with buying (0) and ``