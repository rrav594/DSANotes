class Solution:
    def findMid(self, head):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if count % 2 else slow.next.data
