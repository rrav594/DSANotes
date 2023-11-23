# 1) Tabulation
class Solution:
    def LCSof3(self,A,B,C,n1,n2,n3):
        # code here
        dp = [[[-1 for i in range(n3+1)]for i in range(n2+1)]for j in range(n1+1)]
        for i in range(n1+1):
            for j in range(n2+1):
                for k in range(n3+1):
                    if i == 0 or j == 0 or k == 0:
                        dp[i][j][k] = 0
                    elif A[i-1] == B[j-1] == C[k-1]:
                        dp[i][j][k] = 1 + dp[i-1][j-1][k-1]
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
        return dp[n1][n2][n3]
    


# 2) Memoization
class Solution:
def LCSof3(self,A,B,C,n1,n2,n3):
    # code here
    def helper(A, B, C, i, j, k, dp):
        if dp[i][j][k] != -1:
            return dp[i][j][k]
        if i == 0 or j == 0 or k == 0:
            return 0
        if A[i-1] == B[j-1] == C[k-1]:
            dp[i][j][k] = 1 + helper(A, B, C, i-1, j-1, k-1,dp)
            return dp[i][j][k]
        else:
            dp[i][j][k] = max(helper(A,B,C,i-1,j,k,dp), helper(A,B,C,i,j-1,k,dp), helper(A,B,C,i,j,k-1,dp))
            return dp[i][j][k]
    dp = [[[-1 for i in range(n3+1)]for i in range(n2+1)]for i in range(n1+1)]
    return helper(A,B,C,n1,n2,n3,dp)