class Solution:
	def setBits(self, n):
		# code here
		count = 0
		while n:
		    count += 1
		    n = n & (n-1)
        return count