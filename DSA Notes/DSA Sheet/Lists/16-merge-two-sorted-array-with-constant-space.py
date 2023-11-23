# Shell Sort or gap method
class Solution:
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        def swapIfGreater(arr1, arr2, i, j):
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
        len_arr = n+m
        gap = len_arr//2 + (len_arr%2)
        while gap > 0:
            left = 0
            right = left+gap
            while right < len_arr:
                if left < n and right >= n:
                    swapIfGreater(arr1, arr2, left, right-n)
                elif left >= n:
                    swapIfGreater(arr2, arr2, left-n, right-n)
                else:
                    swapIfGreater(arr1, arr1, left, right)
                left += 1
                right += 1
            if gap == 1:
                break
            gap = gap//2 + gap%2



class Solution:
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        left, right = n-1, 0
        while left >=0 and right < m:
            if arr1[left] > arr2[right]:
                arr1[left], arr2[right] = arr2[right], arr1[left]
                left -= 1
                right += 1
            else:
                break
        arr1.sort()
        arr2.sort()