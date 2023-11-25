class Solution:
    #Function to find first node if the linked list has a loop.
    def findFirstNode(self, head):
        #code here
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast:
            return -1
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast.data
