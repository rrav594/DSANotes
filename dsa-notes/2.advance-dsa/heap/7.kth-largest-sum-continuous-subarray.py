import heapq
class Solution:
    def kthLargest(self, N : int, K : int, Arr : List[int]) -> int:
        sum_ = []
        sum_.append(Arr[0])
        for i in range(1, N):
            sum_.append(sum_[i-1]+Arr[i])
        heap = []
        for i in range(N):
            for j in range(i, N):
                if i == 0:
                    x = sum_[j]
                else:
                    x = sum_[j]-sum_[i-1]
                if len(heap) < K:
                    heapq.heappush(heap, x)
                else:
                    if heap[0] < x:
                        heapq.heappop(heap)
                        heapq.heappush(heap, x)
        return heap[0]