https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        i = 0
        res = []
        while i < n-2:
            # while i+1 < n-2 and nums[i] == nums[i+1]:
            #     i += 1
            start = i+1
            end = n-1
            while start < end:
                # while start+1 < end and nums[start] == nums[start+1]:
                #     start += 1
                # while end-1 > start and nums[end] == nums[end-1]:
                #     end -= 1
                sum_ = nums[i]+nums[start]+nums[end]
                if sum_ == 0:
                    if [nums[i], nums[start], nums[end]] not in res:
                        res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                elif sum_ < 0:
                    start += 1
                else:
                    end -= 1
            i += 1
        return res
    



    # Optimixed
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        i = 0
        res = []
        while i < n-2:
            if i>0 and nums[i] == nums[i-1]:
                i += 1
                continue
            start = i+1
            end = n-1
            while start < end:

                sum_ = nums[i]+nums[start]+nums[end]
                if sum_ == 0:
                    # if [nums[i], nums[start], nums[end]] not in res:
                    res.append([nums[i], nums[start], nums[end]])
                    while start+1 < end and nums[start] == nums[start+1]:
                        start += 1
                    while end-1 > start and nums[end] == nums[end-1]:
                        end -= 1
                    start += 1
                    end -= 1
                    # while start < end and nums[start] == nums[start-1]:
                    #     start += 1
                    # while start < end and nums[end] == nums[end+1]:
                    #     end -= 1
                elif sum_ < 0:
                    start += 1
                else:
                    end -= 1
            i += 1
        return res
        