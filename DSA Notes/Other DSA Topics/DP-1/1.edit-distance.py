# 1) Tabulation
class Solution:
	def editDistance(self, s, t):
		# Code here
		m, n = len(s), len(t)
		dp = [[0 for i in range(n+1)]for j in range(m+1)]
		for i in range(m+1):
		    for j in range(n+1):
		        if i == 0:
		            dp[i][j] = j
		        elif j == 0:
		            dp[i][j] = i
		        elif s[i-1] == t[j-1]:
		            dp[i][j] = dp[i-1][j-1]
		        else:
		            dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
	    return dp[m][n]

# 2) Memoization
class Solution:
    def editDistance(self, s, t):
        # Code here
        def editDistHelper(s, t, m, n, dp):
            if m == 0:
                return n
            if n == 0:
                return m
            if dp[m][n] != -1:
                return dp[m][n]
            if s[m-1] == t[n-1]:
                if dp[m-1][n-1] == -1:
                    dp[m][n] = editDistHelper(s, t, m-1, n-1, dp)
                    return dp[m][n]
                else:
                    dp[m][n] = dp[m-1][n-1]
                    return dp[m][n]
            else:
                if dp[m-1][n] != -1:
                    ins = dp[m-1][n]
                else:
                    ins = editDistHelper(s, t, m-1, n, dp)
                if dp[m][n-1] != -1:
                    rem = dp[m][n-1]
                else:
                    rem = editDistHelper(s, t, m, n-1, dp)
                if dp[m-1][n-1] != -1:
                    rep = dp[m-1][n-1]
                else:
                    rep = editDistHelper(s, t, m-1, n-1, dp)
                dp[m][n] = 1 + min(ins, rem, rep)
                return dp[m][n]
        m, n = len(s), len(t)
        dp = [[-1 for i in range(n+1)]for i in range(m+1)]
        editDistHelper(s, t, m, n, dp)
        return dp[m][n]
    
# 3) Recursion
class Solution:
    def editDistance(self, s, t):
        # Code here
        def editDistHelper(s, t, m, n):
            if m == 0:
                return n
            if n == 0:
                return m
            if s[m-1] == t[n-1]:
                return editDistHelper(s, t, m-1, n-1)
            return 1 + min(editDistHelper(s, t, m, n-1), editDistHelper(s, t, m-1, n), editDistHelper(s, t, m-1, n-1))
        m, n = len(s), len(t)
        return editDistHelper(s, t, m, n)
        