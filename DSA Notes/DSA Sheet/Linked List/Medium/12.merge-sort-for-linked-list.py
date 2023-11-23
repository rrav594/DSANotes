# 1) Method 1
class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        mid = self.findMid(head)
        first, second = head, mid.next
        mid.next = None
        first = self.mergeSort(first)
        second = self.mergeSort(second)
        return self.merge(first, second)
    
    def merge(self, first, second):
        dummy = Node(0)
        curr = dummy
        while first and second:
            if first.data <= second.data:
                curr.next = first
                first = first.next
            else:
                curr.next = second
                second = second.next
            curr = curr.next
        curr.next = first or second
        return dummy.next
    
    def findMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
        return slow


# 2) Method 2
class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
        mid = slow.next
        slow.next = None
        left, right = self.mergeSort(head), self.mergeSort(mid)
        dummy = Node(0)
        curr = dummy
        while left and right:
            if left.data < right.data:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left or right
        return dummy.next