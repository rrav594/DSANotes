class Solution:
    def findMinDiff(self, A,N,M):
        A.sort()
        min_diff = float("inf")
        if M > N:
            return -1
        for i in range(N-M+1):
            min_diff = min(min_diff, A[i+M-1]-A[i])
        return min_diff
