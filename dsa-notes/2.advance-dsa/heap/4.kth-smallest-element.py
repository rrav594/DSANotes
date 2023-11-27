import heapq
class Solution:
    def kthSmallest(self,arr, l, r, k):
        heap = []
        for i in range(k):
            heapq.heappush(heap, -arr[l+i])
        for i in range(k, r+1):
            heapq.heappush(heap, -arr[l+i])
            if len(heap) > k:
                heapq.heappop(heap)
        return -heap[0]
