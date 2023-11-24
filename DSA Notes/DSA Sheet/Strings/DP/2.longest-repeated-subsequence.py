class Solution:
	def LongestRepeatingSubsequence(self, str):
		# Code here
		n = len(str)
		dp = [[0 for i in range(n+1)]for i in range(n+1)]
		for i in range(n+1):
		    for j in range(n+1):
		        if i == 0 or j == 0:
		            dp[i][j] = 0
		        elif str[i-1] == str[j-1] and i != j:
		            dp[i][j] = dp[i-1][j-1] + 1
		        else:
		            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	    return dp[n][n]