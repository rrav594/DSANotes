https://leetcode.com/problems/set-matrix-zeroes/description/

# Space is O(row+col)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        row, col = [0]*n, [0]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j] = 0

# Space optimized
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        col0 = 1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        col0 = 0
                    else:
                        matrix[0][j] = 0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] != 0:
                    if matrix[0][j] == 0 or matrix[i][0] == 0:
                        matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0
        return matrix