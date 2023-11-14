# 1) Recursion
class Solution:
    def equalPartition(self, N, arr):
        # code here
        def helper(n, arr, sum_):
            if sum_ == 0:
                return True
            if n == 0 and sum_ != 0:
                return False
            if arr[n-1] > sum_:
                return helper(n-1, arr, sum_)
            return helper(n-1, arr, sum_) or helper(n-1, arr, sum_-arr[n-1])
        sum_ = sum(arr)
        if sum_ % 2:
            return False
        return helper(N, arr, sum_//2)
    
# 2) Memoization
class Solution:
    def equalPartition(self, N, arr):
        # code here
        def helper(arr, n, sum_, dp):
            if sum_ == 0:
                return True
            if n ==0 and sum != 0:
                return False
            if dp[n][sum_] != -1:
                return dp[n][sum_]
            if arr[n-1] > sum_:
                return helper(arr, n-1, sum_, dp)
            dp[n][sum_] = helper(arr, n-1, sum_, dp) or helper(arr, n-1, sum_-arr[n-1], dp)
            return dp[n][sum_]
        sum_ = sum(arr)
        if sum_ % 2:
            return False
        dp = [[-1 for i in range(sum_//2+1)]for i in range(N+1)]
        return helper(arr, N, sum_//2, dp)

# 3) Tabulation
class Solution:
    def equalPartition(self, N, arr):
        # code here
        sum_ = sum(arr)
        if sum_ % 2:
            return False
        dp = [[False for i in range(sum_//2 + 1)]for i in range(N+1)]
        for i in range(N+1):
            for j in range(sum_//2 + 1):
                if i == 0:
                    dp[i][j] = False
                elif j == 0:
                    dp[i][j] = True
                elif j < arr[i-1]:
                    dp[i][j] = dp[i-1][j] 
                elif j >= arr[i-1]:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
        return dp[N][sum_//2]