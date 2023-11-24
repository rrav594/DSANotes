class Solution:
	def distinctSubsequences(self, S):
		# code here
		mod = 10**9+7
		dp = [0]*(len(S)+1)
		dp[0] = 1
		i = 1
		d = {}
		while i < len(dp):
		    dp[i] = (dp[i-1]*2)%mod
		    c = S[i-1]
		    if c in d:
		        dp[i] = (dp[i]-dp[d[c]-1])%mod
		    d[c] = i
		    i += 1
	    return dp[len(S)]