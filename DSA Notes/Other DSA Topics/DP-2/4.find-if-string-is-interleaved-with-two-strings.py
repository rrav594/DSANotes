# 3) Tabulation
class Solution:
    #function should return True/False
    def isInterleave(self, A, B, C):
        # Code here
        dp = [[False for i in range(len(B)+1)]for i in range(len(A)+1)]
        if len(A)+len(B) != len(C):
            return False
        for i in range(len(A)+1):
            for j in range(len(B)+1):
                if i == 0 and j == 0:# two empty strings have an empty string as interleaving 
                    dp[i][j] = True
                elif i == 0: # A is empty
                    if B[j-1] == C[j-1]:
                        dp[i][j] = dp[i][j-1]
                elif j == 0:# B is empty 
                    if A[i-1] == C[i-1]:
                        dp[i][j] = dp[i-1][j]
                elif A[i-1] == C[i+j-1] and B[j-1] != C[i+j-1]: # Current character of C matches with current character of A, but doesn't match with current character of B 
                    dp[i][j] = dp[i-1][j] 
                elif A[i-1] != C[i+j-1] and B[j-1] == C[i+j-1]: # Current character of C matches with current character of B, but doesn't match with current character of A 
                    dp[i][j] = dp[i][j-1]
                elif A[i-1] == C[i+j-1] == B[j-1]: # Current character of C matches with that of both A and B 
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[len(A)][len(B)]


# 2) Memoization(Top-Down)
class Solution:
    #function should return True/False
    def isInterleave(self, A, B, C):
        # Code here
        def dfs(i, j, A, B, C):
            if dp[i][j] != -1:
                return dp[i][j]
            n, m = len(A), len(B)
            if i == n and j == m:
                return 1
            if i<n and A[i] == C[i+j] and j<m and B[j] == C[i+j]:
                x = dfs(i+1, j, A, B, C)
                y = dfs(i, j+1, A, B, C)
                dp[i][j] = x or y
                return dp[i][j]
            if i < n and A[i] == C[i+j]:
                x = dfs(i+1, j, A, B, C)
                dp[i][j] = x
                return dp[i][j]
            if j < m and B[j] == C[i+j]:
                x = dfs(i, j+1, A, B, C)
                dp[i][j] = x
                return dp[i][j]
            dp[i][j] = 0
            return dp[i][j]
        dp = [[-1 for i in range(len(B)+1)]for i in range(len(A)+1)]
        if len(A)+len(B) != len(C):
            return False
        return dfs(0,0,A,B,C)



# 1) Recursion
class Solution:
    #function should return True/False
    def isInterleave(self, A, B, C):
        # Code here
        if not A and not B and not C:
            return True
        if not C:
            return False
        if A and C[0] == A[0]:
            return self.isInterleave(A[1:], B, C[1:])
        if B and C[0] == B[0]:
            return self.isInterleave(A, B[1:], C[1:])
        return False
    
class Solution:
    #function should return True/False
    def isInterleave(self, A, B, C):
        i, j, k = 0, 0, 0
        while k != len(C)-1:
            if i < len(A) and A[i] == C[k]:
                i += 1
            elif j < len(B) and B[j] == C[k]:
                j += 1
            else:
                return False
            k += 1
        if A[i-1] or B[j-1]:
            return False
        return True
    
# Both of above works only if there are no common characters