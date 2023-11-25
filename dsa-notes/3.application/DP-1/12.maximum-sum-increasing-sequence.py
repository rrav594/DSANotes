class Solution:
	def maxSumIS(self, arr, n):
		# code here
		max_ = 0
		mlis = [0 for i in range(n)]
		for i in range(n):
		    mlis[i] = arr[i]
	    for i in range(1, n):
	        for j in range(i):
	            if arr[i] > arr[j] and mlis[i] < mlis[j] + arr[i]:
	                mlis[i] = mlis[j] + arr[i]
	    for i in range(n):
	        if max_ < mlis[i]:
	            max_ = mlis[i]
	    return max_