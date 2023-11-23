class Solution:  
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        inclusive, exclusive = 0, 0
        for item in a:
            new_exclusive = max(inclusive, exclusive)
            inclusive = exclusive + item
            exclusive = new_exclusive
        return max(inclusive, exclusive)
        
# 1, 3, 6, 9, 13
# inc, exc = 0, 0
# item = 1.....
# new_exc = 0, inc = 0+1, exc = 0
# item = 3.....
# new_exc = 1, inc = 0+3, exc = 1
# item = 6.....
# new_exc = 3, inc = 1+6, exc = 3
# item = 9.....
# new_exc = 7, inc = 3+9, exc = 7
# item = 13.....
# new_exc = 12, inc = 7+13, exc = 12