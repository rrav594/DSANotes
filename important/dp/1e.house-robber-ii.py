class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums, n):
            prev2, prev = float("-inf"), nums[0]
            for i in range(1, n):
                pick = nums[i]+prev2 if prev2 != float("-inf") else nums[i]
                notPick = prev

                prev2 = prev
                prev = max(pick, notPick)
            return prev
        if len(nums) == 1:
            return nums[0]
        arr1, arr2 = [], []
        arr1[:] = nums[:-1]
        arr2[:] = nums[1:]
        ans1 = helper(arr1, len(arr1))
        ans2 = helper(arr2, len(arr2))
        return max(ans1, ans2)