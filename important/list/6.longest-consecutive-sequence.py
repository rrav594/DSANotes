class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return 1
        s = set(nums)
        longest = 1
        for i in range(n):
            if nums[i]-1 not in s:
                count = 1
                x = nums[i]+1
                while x in s:
                    count += 1
                    x += 1
                longest = max(longest, count)
        return longest
