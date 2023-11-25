class Solution:
    def nextPermutation(self, N, arr):
        # code here
        k = N-2
        while k >= 0:
            if arr[k] < arr[k+1]:
                break
            k -= 1
        if k == -1:
            return arr[::-1]
        i = N-1
        while i > k:
            if arr[i] > arr[k]:
                break
            i -= 1
        arr[i], arr[k] = arr[k], arr[i]
        arr[k+1:] = reversed(arr[k+1:])
        return arr