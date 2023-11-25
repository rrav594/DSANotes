class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()#r+c is constant
        negDiag = set()#r-c is constant
        res = []
        board = [["." for i in range(n)]for i in range(n)]
        def backTrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or r+c in posDiag or r-c in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backTrack(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        backTrack(0)
        return res



