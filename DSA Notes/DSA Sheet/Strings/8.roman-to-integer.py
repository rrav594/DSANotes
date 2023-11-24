class Solution:
    def romanToDecimal(self, S): 
        # code here
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = 0
        for i in range(len(S)-1):
            if d[S[i]] < d[S[i+1]]:
                res -= d[S[i]]
            else:
                res += d[S[i]]
        res += d[S[-1]]
        return res