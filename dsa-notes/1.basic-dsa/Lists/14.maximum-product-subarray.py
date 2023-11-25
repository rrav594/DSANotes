class Solution:
	# Function to find maximum product subarray
	def maxProduct(self,arr, n):
	    minVal, maxVal, ans = arr[0], arr[0], arr[0]
	    for i in range(1, n):
	        if arr[i] < 0:
	            minVal, maxVal = maxVal, minVal
	        minVal = min(minVal*arr[i], arr[i])
	        maxVal = max(maxVal*arr[i], arr[i])
	        ans = max(ans, maxVal)
	    return ans