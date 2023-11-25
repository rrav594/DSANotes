# Using sliding window
class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        count = 0
        start, end = 0, 0
        p = 1
        while end < n:
            p *= a[end]
            while start < end and p >= k:
                p //= a[start]
                start += 1
            if p < k:
                l = end-start+1
                count += l
            end += 1
        return count
            