https://leetcode.com/problems/majority-element-ii/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2 = 0, 0
        candidate1, candidate2 = float("-inf"), float("-inf")
        n = len(nums)
        for i in range(n):
            if count1 == 0 and candidate2 != nums[i]:
                count1 = 1
                candidate1 = nums[i]
            elif count2 == 0 and candidate1 != nums[i]:
                count2 = 1
                candidate2 = nums[i]
            elif candidate1 == nums[i]:
                count1 += 1
            elif candidate2 == nums[i]:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1 , count2 = 0, 0
        for i in range(n):
            if nums[i] == candidate1:
                count1 += 1
            if nums[i] == candidate2:
                count2 += 1
        res = []
        if count1 > n//3:
            res.append(candidate1)
        if count2 > n//3:
            res.append(candidate2)
        return res