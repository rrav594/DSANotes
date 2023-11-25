class Solution:
    def reverseDLL(self, head):
        #return head after reversing
        if head is None:
            return head
        curr = head
        prev = None
        while curr:
            prev = curr
            curr.next, curr.prev = curr.prev, curr.next
            curr = curr.prev
        return prev
