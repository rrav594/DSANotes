class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        def reverse(head):
            curr = head
            prev = None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        head = reverse(head)
        carry, k, prev = 0, head, None
        head.data += 1
        while head and (head.data > 9 or carry > 0):
            prev = head
            head.data += carry
            carry = head.data // 10
            head.data %= 10
            head = head.next
        if carry:
            prev.next = Node(carry)
        head = reverse(k)
        return head