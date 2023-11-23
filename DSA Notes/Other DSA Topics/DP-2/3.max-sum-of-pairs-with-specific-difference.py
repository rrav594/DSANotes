class Solution:
    def maxSumPairWithDifferenceLessThanK(self, arr, N, K): 
        # Your code goes here 
        arr.sort()# Sort input array in ascending order.
        dp = [0] * N
        dp[0] = 0# if no element then dp value will be 0
        for i in range(1, N):
            dp[i] = dp[i-1] # first give previous value to dp[i] i.e. no pairing with (i-1)th element
            if arr[i]-arr[i-1] < K:
                if i>=2:# update dp[i] by choosing maximum between pairing and not pairing
                    dp[i] = max(dp[i], dp[i-2]+arr[i]+arr[i-1])
                else:
                    dp[i] = max(dp[i], arr[i]+arr[i-1])
        return dp[N-1]
 

class Solution:
    def maxSumPairWithDifferenceLessThanK(self, arr, N, K): 
        # Your code goes here 
        arr.sort()
        max_ = 0
        i = N-1
        while i > 0:
        # Case I: Diff of arr[i] and arr[i-1]
        #     is less than K, add to maxSum
        # Case II: Diff between arr[i] and
        #     arr[i-1] is not less than K,
        #     move to next i since with sorting
        #     we know, arr[i]-arr[i-1] < arr[i]-arr[i-2]
        #     and so on.
            if arr[i]-arr[i-1] < K: # Assuming only positive numbers.
                max_ += arr[i]+arr[i-1]
                i -= 1# When a match is found skip this pair
            i -= 1
        return max_

