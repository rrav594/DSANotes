class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
class Solution:
    def maxChainLen(self,Parr, n):
        # Parr:  list of pair
        Parr.sort(key=lambda x:x.b)
        prev = float("-inf")
        ans = 0
        for x in Parr:
            if x.a > prev:
                ans += 1
                prev = x.b
        return ans
    

    # 2) Using LIS
'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''
class Solution:
    def maxChainLen(self,Parr, n):
        # Parr:  list of pair
        Parr.sort(key=lambda x:x.a)
        mcl = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if Parr[i].a > Parr[j].b and mcl[i] < mcl[j]+1:
                    mcl[i] = mcl[j] + 1
        return max(mcl)
        