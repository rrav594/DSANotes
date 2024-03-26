https://leetcode.com/problems/reverse-pairs/submissions/1108157956/

class Solution:
    def inversionCount(self, arr, n):
        # Your Code Here
        def merge(arr, low, mid, high):
            left, right = low, mid+1
            res = []
            count = 0
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    res.append(arr[left])
                    left += 1
                else:
                    res.append(arr[right])
                    count += mid-left+1
                    right += 1
            while left <= mid:
                res.append(arr[left])
                left += 1
            while right <= high:
                res.append(arr[right])
                right += 1
            for i in range(low, high+1):
                arr[i] = res[i-low]
            return count
        def mergesort(arr, low, high):
            count = 0
            if low >= high:
                return count
            mid = (low+high)//2
            count += mergesort(arr, low, mid)
            count += mergesort(arr, mid+1, high)
            count += merge(arr, low, mid, high)
            return count
        return mergesort(arr, 0, n-1)
