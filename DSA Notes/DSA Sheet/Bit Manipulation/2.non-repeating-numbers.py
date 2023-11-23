class Solution:
	def singleNumber(self, nums):
		# Code here
		res = 0
		for i in nums:
		    res = res ^ i
	    res = res & (-res)
	    ans1, ans2 = 0, 0
	    for i in nums:
	        if i & res:
	            ans1 = ans1 ^ i
	        else:
	            ans2 = ans2 ^ i
	    if ans1 > ans2:
	        return [ans2, ans1]
	    return [ans1, ans2]


from collections import Counter
class Solution:
    def singleNumber(self, nums):
        # Code here
        ans = []
        d = Counter(nums)
        for k in d.keys():
            if d[k] > 1:
                continue
            ans.append(k)
        return sorted(ans)