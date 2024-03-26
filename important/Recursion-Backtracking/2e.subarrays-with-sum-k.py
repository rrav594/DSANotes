class Solution:
    def findSubArraySum(self, Arr, N, k):
        # code here
        d = {}
        count = 0
        pre = 0
        d[0] = 1
        for i in range(N):
            pre += Arr[i]
            if pre-k in d:
                count += d[pre-k]
            d[pre] = d.get(pre, 0) + 1
        return count

