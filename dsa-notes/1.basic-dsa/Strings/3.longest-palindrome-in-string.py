class Solution:
    def longestPalin(self, S):
        # code here
        maxLen = 1
        start = 0
        for i in range(len(S)):
            low, high = i-1, i+1
            while low >= 0 and S[i] == S[low]:
                low -= 1
            while high < len(S) and S[i] == S[high]:
                high += 1
            while low >= 0 and high < len(S) and S[low] == S[high]:
                low -= 1
                high += 1
            length = (high-1)-(low+1)+1
            if length > maxLen:
                start = low+1
                maxLen = length
        return S[start:start+maxLen]