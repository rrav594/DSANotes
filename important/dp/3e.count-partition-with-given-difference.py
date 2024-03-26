class Solution:
    def countPartitions(self, n, d, arr):
        total = sum(arr)
        if total-d < 0:
            return 0
        elif (total-d)%2 == 1:
            return 0
        else:
            target = (total-d)//2
            dp = [[-1 for i in range(target+1)]for i in range(n)]
            def helper(n, target):
                if n == 0:
                    if arr[n] == target and target == 0:
                        return 2
                    elif arr[n] == target or target == 0:
                        return 1
                    else:
                        return 0
                if dp[n][target] != -1:
                    return dp[n][target]
                dp[n][target] = helper(n-1, target)
                if arr[n] <= target:
                    dp[n][target] += helper(n-1, target-arr[n])
                return dp[n][target]%(10**9+7)
            return helper(n-1, target)