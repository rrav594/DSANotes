class Solution:
	def overlappedInterval(self, Intervals):
		#Code here
		Intervals.sort(key=lambda x:x[0])
		selected = []
		selected.append(Intervals[0])
		i = 1
		while i < len(Intervals):
		    if Intervals[i][0] > selected[-1][1]:
		        selected.append(Intervals[i])
		    else:
		        selected[-1][1] = max(Intervals[i][1], selected[-1][1])
            i += 1
        return selected