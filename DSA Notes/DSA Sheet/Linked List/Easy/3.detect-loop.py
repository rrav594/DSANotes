# 1) Floyd Cycle Detection Loop
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
# 2) Using Set
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        s = set()
        curr = head
        while curr:
            if curr in s:
                return True
            s.add(curr)
            curr = curr.next
        return False