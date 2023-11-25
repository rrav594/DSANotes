class Solution:
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        ##Your code here
        if n == 0:
            return False
        return n & (n-1) == 0


class Solution:
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        ##Your code here
        count = 0
        while n:
            count += 1
            n = n&(n-1)
        if count == 1:
            return True
        return False