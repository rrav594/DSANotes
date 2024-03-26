class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def backtrack(i, total):
            if total == 0:
                res.append(curr[:])
                return
            if i == len(candidates) or total < 0:
                return
            curr.append(candidates[i])
            backtrack(i, total-candidates[i])
            curr.pop()
            backtrack(i+1, total)
        backtrack(0, target)
        return res
    

class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def bac(i, total):
            if total == target:
                res.append(subset[:])
                return
            if i == len(c) or total > target:
                return
            subset.append(c[i])
            bac(i, total+c[i])
            subset.pop()
            bac(i+1, total)
        bac(0, 0)
        return res
        