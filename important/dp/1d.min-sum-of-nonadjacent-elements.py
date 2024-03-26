class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        def helper(i):
            if i == 0:
                return nums[0]
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i]
            pick = nums[i]+helper(i-2)
            notPick = helper(i-1)
            dp[i] = max(pick, notPick)
            return dp[i]
        return helper(len(nums)-1)


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        for i in range(1, n):
            pick = nums[i]        
            if i-2 >= 0:
                pick += dp[i-2]
            notPick = dp[i-1]
            dp[i] = max(pick, notPick)
        return dp[n-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev, prev2 = nums[0], float("inf")
        for i in range(1, n):
            pick = nums[i]+prev2 if prev2 != float("inf") else nums[i]
            notPick = prev
            prev2 = prev
            prev = max(pick, notPick)
        return prev        