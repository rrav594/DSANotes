class Solution:
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        ##Your code here
        count = 0
        res = a ^ b
        while res:
            count += 1
            res = res & (res-1)
        return count
