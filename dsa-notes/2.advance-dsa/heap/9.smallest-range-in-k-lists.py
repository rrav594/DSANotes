import heapq
class Solution:
    def smallestRange(self, arr, n, k):
        heap = []
        maxx = float("-inf")
        for i in range(k):
            heapq.heappush(heap, [arr[i][0], i, 0])
            maxx = max(maxx, arr[i][0])
        ans = [heap[0][0], maxx]
        diff = maxx-heap[0][0]
        while True:
            minn, arr_ind, val_ind = heapq.heappop(heap)
            if diff > maxx-minn:
                diff = maxx-minn
                ans = [minn, maxx]
            if val_ind+1 >= len(arr[arr_ind]):
                break
            maxx = max(maxx, arr[arr_ind][val_ind+1])
            heapq.heappush(heap, [arr[arr_ind][val_ind+1], arr_ind, val_ind+1])
        return ans