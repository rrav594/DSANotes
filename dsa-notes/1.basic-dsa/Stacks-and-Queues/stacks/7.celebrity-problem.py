class Solution:
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        a, b = 0, n-1
        while a < b:
            if M[a][b]:
                a += 1
            else:
                b -= 1
        for i in range(n):
            if i!=a and (M[a][i] or not M[i][a]):
                return -1
        return a