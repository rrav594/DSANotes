import heapq
class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        heap = []
        for i in range(k):
            heapq.heappush(heap, -arr[l+i])
        for i in range(k, len(arr)):
            heapq.heappush(heap, -arr[l+i])
            while len(heap) > k:
                heapq.heappop(heap)
        return -heap[0]