import heapq
class Solution:
    def kLargest(self,arr, n, k):
        heap = []
        for i in range(n):
            heapq.heappush(heap, -arr[i])
        ans = []
        for i in range(k):
            ans.append(-heapq.heappop(heap))
        return ans