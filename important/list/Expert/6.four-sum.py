https://leetcode.com/problems/4sum/submissions/1108258807/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        i = 0
        res = []
        nums.sort()
        n = len(nums)
        while i < n-3:
            j = i+1
            while j < n-2:
                start, end = j+1, n-1
                while start < end:
                    sum_ = nums[i]+nums[j]+nums[start]+nums[end]
                    if sum_ == target:
                        if [nums[i], nums[j], nums[start], nums[end]] not in res:
                            res.append([nums[i], nums[j], nums[start], nums[end]]) 
                        end -= 1
                        start += 1
                    elif sum_ < target:
                        start += 1
                    else:
                        end -= 1
                j += 1
            i += 1
        return res
        