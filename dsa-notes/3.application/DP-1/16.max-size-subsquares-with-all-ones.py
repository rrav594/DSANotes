class Solution:
    def maxSquare(self, n, m, mat):
        S = [[0 for i in range(m)]for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    S[i][j] = mat[i][j]
                else:
                    S[i][j] = 0
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] == 1:
                    S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
                else:
                    S[i][j] = 0
        max_of_s = S[0][0]
        max_i, max_j = 0, 0
        for i in range(n):
            for j in range(m):
                if max_of_s < S[i][j]:
                    max_of_s = S[i][j]
                    max_i, max_j = i, j
        return max_of_s        
        