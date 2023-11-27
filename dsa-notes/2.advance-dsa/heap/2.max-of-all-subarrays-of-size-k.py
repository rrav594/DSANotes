from collections import deque
class Solution:
    def max_of_subarrays(self,arr,n,k):
        q = deque()
        ans = []
        for i in range(k):
            while q and arr[q[-1]] < arr[i]:
                q.pop()
            q.append(i)
        ans.append(arr[q[0]])
        for i in range(k, n):
            while q and arr[q[-1]] < arr[i]:
                q.pop()
            while q and q[0] <= i-k:
                q.popleft()
            q.append(i)
            ans.append(arr[q[0]])
        return ans




import heapq
class Solution:
    def max_of_subarrays(self,arr,n,k):
        heap = []
        for i in range(k):
            heapq.heappush(heap, [-arr[i], i])
        ans = []
        ans.append(-heap[0][0])
        for i in range(k, n):
            heapq.heappush(heap, [-arr[i], i])
            while heap[0][1] <= (i-k):
                heapq.heappop(heap)
            ans.append(-heap[0][0])
        return ans