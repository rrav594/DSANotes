class Solution:
	def findMaxSum(self,arr, n):
		# code here
		dp = [0 for i in range(n)]
		if n >= 1:
		    dp[0] = arr[0]
	    if n >= 2:
	        dp[1] = arr[0] + arr[1]
	    if n > 2:
	        dp[2] = max(dp[1], arr[1]+arr[2], arr[0]+arr[2])
	    for i in range(3, n):
	        dp[i] = max(dp[i-1], dp[i-2]+arr[i], dp[i-3]+arr[i]+arr[i-1])
	    return dp[n-1]



class Solution:
	def findMaxSum(self,arr, n):
		# code here
		dp = [-1] * (n+1)
		def helper(n):
		    if dp[n] != -1:
		        return dp[n]
		    if n == 0:
		        dp[n] = 0
		        return dp[n]
		    if n == 1:
		        dp[n] = arr[0]
		        return dp[n]
		    if n == 2:
		        dp[n] = arr[1]+arr[0]
		        return dp[n]
		    dp[n] = max(helper(n-1), helper(n-2)+arr[n-1], helper(n-3)+arr[n-1]+arr[n-2])
		    return dp[n]
	    return helper(n)