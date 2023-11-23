class Solution:
    def findPosition(self, N):
        # code here
        if N == 0 or (N & (N-1) != 0):
            return -1
        pos = 0
        while N:
            pos += 1
            N = N >> 1
        return pos
