class Solution:
    def search(self, patt, s):
        # code here
        if len(patt) > len(s):
            return -1
        ans = []
        d = 256
        q = 101
        p, t, = 0, 0 
        h = 1
        m, n = len(patt), len(s)
        for i in range(m-1):
            h = (h*d)%q
        for i in range(m):
            p = (d*p+ord(patt[i]))%q
            t = (d*t+ord(s[i]))%q
        for i in range(n-m+1):
            if p == t:
                for j in range(m):
                    if s[i+j] != patt[j]:
                        break
                    else:
                        j += 1
                if j == m:
                    ans.append(i+1)
            if i < n-m:
                t = (d*(t-ord(s[i])*h)+ord(s[i+m]))%q
                if t < 0:
                    t = t+q
        return ans if ans else [-1]