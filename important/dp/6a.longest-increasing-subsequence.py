
class Solution:
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,arr,n):
        lis = [1]*n
        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
        return max(lis)


# 2) Using binary search- O(NlogN) time complexity and O(N) space
class Solution:
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,arr,n):
        def ceilIndex(tail, x):
            l, r = 0, len(tail)-1
            while r > l:
                m = (l+r)//2
                if tail[m] >= x:
                    r = m
                else:
                    l = m+1
            return r
                    
        tail = [arr[0]]
        for i in range(1, n):
            if arr[i] > tail[-1]:
                tail.append(arr[i])
            else:
                c = ceilIndex(tail, arr[i])
                tail[c] = arr[i]
        return len(tail)