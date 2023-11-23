# 1) Method 1
# Using dummy Node
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        def reverse(head):
            curr = head
            prev = None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        first, second = reverse(first), reverse(second)
        dummy = Node(0)
        curr = dummy
        carry = 0
        while first or second:
            total = 0 + carry
            if first:
                total += first.data
                first = first.next
            if second:
                total += second.data
                second = second.next
            carry = total // 10
            total = total % 10
            curr.next = Node(total)
            curr = curr.next
        if carry:
            curr.next = Node(carry)
        return reverse(dummy.next)
    

# 2) Method 2
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        def reverse(head):
            curr = head
            prev = None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        first, second = reverse(first), reverse(second)
        carry, total = 0, 0
        head = first
        while first and second:
            total = carry + first.data + second.data
            carry = total // 10
            first.data = total % 10
            prev = first
            first, second = first.next, second.next
            total = 0
        if first or second:
            if second:
                prev.next = second
            first = prev.next
            while first:
                total = first.data + carry
                first.data = total % 10
                carry = total // 10
                prev = first
                first = first.next
        if carry:
            prev.next = Node(carry)
        return reverse(head)