import heapq
class Solution():
    def mergeHeaps(self, a, b, n, m):
        heap = []
        heap[:] = a+b
        heapq.heapify(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap))
        return res[::-1]
    



class Solution():
    def mergeHeaps(self, a, b, n, m):
        def maxHeapify(arr, n, i):
            left = 2*i+1
            right = 2*i+2
            largest = i
            if left < n and arr[largest] < arr[left]:
                largest = left
            if right < n and arr[largest] < arr[right]:
                largest = right
            if i != largest:
                arr[i], arr[largest] = arr[largest], arr[i]
                maxHeapify(arr, n, largest)
        def buildHeap(arr, n):
            for i in range((n-2)//2, -1, -1):
                maxHeapify(arr, n, i)
        merged = []
        merged[:] = a+b
        buildHeap(merged, len(merged))
        return merged