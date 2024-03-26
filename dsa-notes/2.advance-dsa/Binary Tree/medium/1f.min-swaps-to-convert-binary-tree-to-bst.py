class Solution:
    def minSwaps(self, n : int, A : List[int]) -> int:
        # code here
        ans = []
        def inorder(i):
            if i >= n:
                return 
            inorder(2*i+1)
            ans.append(A[i])
            inorder(2*i+2)
        inorder(0)
        swaps = 0
        arr = sorted((ele, i) for i, ele in enumerate(ans))
        i = 0
        while i < len(arr):
            if arr[i][1] == i:
                i += 1
            else:
                index = arr[i][1]
                arr[index], arr[i] = arr[i], arr[index]
                swaps += 1
        return swaps