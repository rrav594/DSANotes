class Key:
    def __init__(self, data, ll):
        self.val = data
        self.ll = ll
    def __lt__(self, other):
        return True if self.val < other.val else False
import heapq
class Solution:
    #Function to merge K sorted linked list.
    def mergeKLists(self,arr,K):
        heap = []
        for i in range(K):
            heapq.heappush(heap, Key(arr[i].data, arr[i]))
        dummy = Node(0)
        curr = dummy
        while heap:
            key = heapq.heappop(heap)
            curr.next = key.ll
            curr = curr.next
            if key.ll.next is not None:
                heapq.heappush(heap, Key(key.ll.next.data, key.ll.next))
        return dummy.next