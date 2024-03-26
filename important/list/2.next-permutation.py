https://leetcode.com/problems/next-permutation/submissions/1108295660/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        k = n-2
        while k >= 0:
            if nums[k] < nums[k+1]:
                break
            k -= 1
        if k == -1:
            return nums.reverse()
        for i in range(n-1, k, -1):
            if nums[i] > nums[k]:
                break
        nums[i], nums[k] = nums[k], nums[i]
        nums[k+1:] = reversed(nums[k+1:])
        return nums       