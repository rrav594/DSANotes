class Solution:
    def maxSum (self, w, x, b, n):
        #code here
        d = {}
        for i in range(n):
            d[x[i]] = b[i]
        max_ = float("-inf")
        max_ending_here = 0
        start, end = 0, 0
        s = 0
        for i in range(len(w)):
            ele = d[w[i]] if w[i] in d else ord(w[i])
            max_ending_here += ele
            if max_ < max_ending_here:
                max_ = max_ending_here
                start = s
                end = i
            if max_ending_here < 0:
                max_ending_here = 0
                s = i+1
        return w[start:end+1]