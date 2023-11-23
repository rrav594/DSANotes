class Solution:
    def inversionCount(self, arr, n):
        # Your Code Here
        def merge(arr, l, m, h):
            inv = 0
            left = arr[l:m+1]
            right = arr[m+1:h+1]
            i, j, k = 0, 0, l
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    inv += len(left)-i
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
            return inv
        def mergeSort(arr, l, h):
            inv = 0
            if l < h:
                mid = (l+h)//2
                inv += mergeSort(arr, l, mid)
                inv += mergeSort(arr, mid+1, h)
                inv += merge(arr, l, mid, h)
            return inv
        return mergeSort(arr, 0, n-1)