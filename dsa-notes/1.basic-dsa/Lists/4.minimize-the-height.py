class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        min_, max_ = arr[0], arr[n-1]
        diff = arr[n-1]-arr[0] 
        for i in range(n):
            if arr[i]-k < 0:
                continue
            min_ = min(arr[0]+k, arr[i]-k)
            max_ = max(arr[i-1]+k, arr[n-1]-k)
            diff = min(diff, max_-min_)
        return diff