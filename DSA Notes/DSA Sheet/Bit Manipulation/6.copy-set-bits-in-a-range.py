class Solution:
    def setAllRangeBits(self, N , L , R):
        # code here
        for i in range(L-1, R):
            N = N | (1 << i)
        return N