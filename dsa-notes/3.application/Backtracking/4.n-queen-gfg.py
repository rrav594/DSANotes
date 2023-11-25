class Solution:
    def nQueen(self, n):
        # code here
        col, posDiag, negDiag = set(), set(), set()
        board = [[0 for i in range(n)]for i in range(n)]
        res = []
        def backTrack(r):
            if r == n:
                v = []
                for i in range(n):
                    for j in range(n):
                        if board[i][j] == 1:
                            v.append(j+1)
                res.append(v)
                return
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = 1
                
                backTrack(r+1)
                
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = 0
        backTrack(0)
        return res