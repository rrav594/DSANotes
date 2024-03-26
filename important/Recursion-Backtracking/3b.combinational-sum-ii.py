class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()
        def backtrack(i, total):
            if total == target:
                res.append(subset[:])
                return
            if i == len(candidates) or total > target:
                return
            subset.append(candidates[i])
            backtrack(i+1, total+candidates[i])
            subset.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, total)
        backtrack(0, 0)
        return res
    


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()
        
        def backtrack(i, total):
            if total == target:
                res.append(subset[:])
            if total >= target:
                return 
            prev = -1
            for i in range(i, len(candidates)):
                if candidates[i] == prev:
                    continue
                subset.append(candidates[i])
                backtrack(i+1, total+candidates[i])
                subset.pop()
                prev = candidates[i]
        backtrack(0, 0)
        return res