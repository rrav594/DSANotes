# 1) Kadane Algorithm
class Solution:
    def maxSubstring(self, S):
        # code here
        n=len(S)
        cur=0
        mx=0
        for i in range(0,n):
            if S[i]=='0':
                cur+=1
            else:
                cur-=1
            if cur<0:
                cur=0
            mx=max(mx,cur)
        if mx:
            return mx
        else:
            return -1
            
        