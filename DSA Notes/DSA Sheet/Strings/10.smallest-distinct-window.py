class Solution:
    def findSubString(self, str):
        # Your code goes here
        minLen = float("inf")
        length = len(set(str))
        d = {}
        start, end = 0, 0
        while end < len(str):
            d[str[end]] = d.get(str[end], 0)+1
            if len(d) == length:
                while d[str[start]] > 1:
                    d[str[start]] -= 1
                    start += 1
                minLen = min(minLen, end-start+1)
            end += 1
        return minLen