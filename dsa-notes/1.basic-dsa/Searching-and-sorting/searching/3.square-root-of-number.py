class Solution:
    def floorSqrt(self, x): 
    #Your code here
        i, j = 0, x
        ans = 0
        while i <= j:
            mid = (i+j)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                ans = mid
                i = mid+1
            else:
                j = mid-1
        return ans