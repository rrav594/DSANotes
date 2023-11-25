class Solution:
    def trappingWater(self, arr,n):
        #Code here
        left, right = [-1]*n, [-1]*n
        left[0] = arr[0]
        right[n-1] = arr[n-1]
        for i in range(1, n):
            left[i] = max(left[i-1], arr[i])
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], arr[i])
        total = 0
        for i in range(1, n-1):
            total += min(left[i], right[i])-arr[i]
        return total