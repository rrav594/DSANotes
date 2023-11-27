import heapq
class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, k):
        heap = []
        res = []
        for i in range(k):
            heapq.heappush(heap, [arr[i][0], i, 0])
        while heap:
            val, arr_ind, val_ind = heapq.heappop(heap)
            res.append(val)
            if val_ind+1 < len(arr[arr_ind]):
                heapq.heappush(heap, [arr[arr_ind][val_ind+1], arr_ind, val_ind+1])
        return res