class Solution:
    def minSwap (self,arr, n, k) : 
        #Complete the function
        count = 0
        for i in range(n):
            if arr[i] <= k:
                count += 1
        bad = 0
        for i in range(count):
            if arr[i] > k:
                bad += 1
        ans = bad
        j = count
        for i in range(n-count):
            if arr[i] > k:
                bad -= 1
            if arr[j] > k:
                bad += 1
            ans = min(ans, bad)
            j += 1
        return ans
        # for i in range(n):
        #     if j == n:
        #         break
        #     if arr[i] > k:
        #         bad -= 1
        #     if arr[j] > k:
        #         bad += 1
        #     ans = min(ans, bad)
        #     j += 1
    






