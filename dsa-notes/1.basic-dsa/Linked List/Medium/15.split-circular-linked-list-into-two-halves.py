class Solution:
    def splitList(self, head, head1, head2):
        slow = head
        fast = head.next
        while fast != head and fast.next != head:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = head1
        curr = head2
        while curr.next != head:
            curr = curr.next
        curr.next = head2
        return head1, head2