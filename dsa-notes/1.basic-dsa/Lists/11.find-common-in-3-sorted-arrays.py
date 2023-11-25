class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        i, j, k = 0, 0, 0
        common = []
        while i < n1 and j < n2 and k < n3:
            while i < n1-1 and A[i] == A[i+1]:
                i += 1
            while j < n2-1 and B[j] == B[j+1]:
                j += 1
            while k < n3-1 and C[k] == C[k+1]:
                k += 1
            if A[i] == B[j] == C[k]:
                common.append(A[i])
                i += 1
                j += 1
                k += 1
            elif A[i] < B[j]:
                i += 1
            elif B[j] < C[k]:
                j += 1
            else:
                k += 1
        # common = list(set(common))
        common.sort()
        return common
