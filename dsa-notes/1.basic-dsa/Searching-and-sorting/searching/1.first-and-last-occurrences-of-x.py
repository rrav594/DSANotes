class Solution:
    def find(self, arr, n, x):
        i, j = 0, n-1
        first, last = -1, -1
        while i <= j:
            mid = (i+j)//2
            if arr[mid] == x:
                first, last = mid, mid
                while first-1 >= 0 and arr[first-1] == arr[first]:
                    first -= 1
                while last+1 < n and arr[last] == arr[last+1]:
                    last += 1
                return [first, last]
            elif arr[mid] < x:
                i = mid+1
            else:
                j = mid-1
        return [-1, -1]