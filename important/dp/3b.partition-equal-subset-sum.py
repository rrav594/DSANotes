class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_%2:
            return False
        else:
            target = sum_//2
            dp = [[-1 for i in range(target+1)]for i in range(len(nums))]
            def helper(n, target):
                if dp[n][target] != -1:
                    return dp[n][target]
                if n == 0:
                    return nums[0]==target 
                notPick = helper(n-1, target)
                pick = False       
                if nums[n] <= target:
                    pick = helper(n-1, target-nums[n])
                dp[n][target] = pick or notPick
                return dp[n][target]
            return helper(len(nums)-1, target)



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_%2:
            return False
        else:
            target = sum_//2
            dp = [[False for i in range(target+1)]for i in range(len(nums))]
            for i in range(len(nums)):
                for j in range(target+1):
                    if j == 0:
                        dp[i][j] = True
                        continue
                    if i == 0 and nums[i] == target:
                        dp[i][j] = True
                        continue
                    notPick = dp[i-1][j]
                    pick = False
                    if nums[i] <= target:
                        pick = dp[i-1][j-nums[i]]
                    dp[i][j] = pick or notPick
            return dp[len(nums)-1][target]