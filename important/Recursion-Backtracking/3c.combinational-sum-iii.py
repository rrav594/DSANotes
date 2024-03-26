class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []
        subset = []
        def backtrack(i, total):
            if total == n:
                if len(subset) == k:
                    res.append(subset[:])
                return
            if i == len(nums) or total > n:
                return
            subset.append(nums[i])
            backtrack(i+1, total+nums[i])
            subset.pop()
            backtrack(i+1, total)
        backtrack(0, 0)
        return res
        