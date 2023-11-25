class Solution:
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, n, sum):
        mydict = dict()
        pre_sum = 0
        count = 0
        for i in range(n):
            pre_sum += arr[i]
            if pre_sum == sum:
                count += 1
            if pre_sum-sum in mydict:
                count += mydict[pre_sum-sum]
            if pre_sum not in mydict:
                mydict[pre_sum] = 0
            mydict[pre_sum] += 1
        return count
      
