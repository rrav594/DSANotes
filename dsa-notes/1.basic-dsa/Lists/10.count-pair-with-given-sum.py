class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        count = 0
        d = {}
        for i in range(n):
            if k-arr[i] in d:
                count += d[k-arr[i]]
            d[arr[i]] = d.get(arr[i], 0) + 1
        return count