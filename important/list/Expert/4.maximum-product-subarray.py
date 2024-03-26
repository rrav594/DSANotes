https://leetcode.com/problems/maximum-product-subarray/

# It is solved in O(n^2) time.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ = float("-inf")
        n = len(nums)
        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod *= nums[j]
                max_ = max(prod, max_)
        return max_


Optimal Solution
Keep calculating suffix and prefix of product

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre, suf = 1, 1
        ans = float("-inf")
        n = len(nums)
        for i in range(n):
            if pre == 0:
                pre = 1
            if suf == 0:
                suf = 1
            pre = pre*nums[i]
            suf = suf*nums[n-i-1]
            ans = max(ans, pre, suf)
        return ans 