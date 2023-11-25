class Solution:
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        d = {}
        sum_ = 0
        for i in range(n):
            sum_ += arr[i]
            if sum_ == 0 or sum_ in d:
                return True
            d[sum_] = d.get(sum_, 0) + 1
        return False