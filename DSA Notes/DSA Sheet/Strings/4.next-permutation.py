class Solution:
    def nextPermutation(self, N, arr):
        # code here
        end = N-2
        while end >= 0:
            if arr[end] < arr[end+1]:
                break
            end -= 1
        if end == -1:
            return arr[::-1]
        for i in range(N-1, end, -1):
            if arr[i] > arr[end]:
                break
        arr[i], arr[end] = arr[end], arr[i]
        arr[end+1:] = reversed(arr[end+1:])
        return arr