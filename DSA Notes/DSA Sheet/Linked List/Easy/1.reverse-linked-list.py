# 1) Iterative
class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
# 2) Recursion
class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        if head is None or head.next is None:
            return head
        rest = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rest