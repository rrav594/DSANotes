class Solution:
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, N):
        #code here
        s = set()
        start = 0
        count = 0
        for i in arr:
            s.add(i)
        for i in arr:
            if i-1 not in s:
                start = i
                while start in s:
                    start += 1
                count = max(count, start-i)
        return count

