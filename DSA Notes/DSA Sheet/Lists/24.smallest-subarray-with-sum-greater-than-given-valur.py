class Solution:
    def smallestSubWithSum(self, a, n, x):
        # Your code goes here
        start, total = 0, 0 
        res = float("inf")
        for end in range(len(a)):
            total += a[end]
            while total > x:
                res = min(res, end-start+1)
                total -= a[start]
                start += 1
        return 0 if res == float("inf") else res