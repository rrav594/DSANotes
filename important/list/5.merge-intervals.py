https://leetcode.com/problems/merge-intervals/description/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        selected = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= selected[-1][1]:
                selected[-1][1] = max(selected[-1][1], intervals[i][1])
            else:
                selected.append(intervals[i])
        return selected