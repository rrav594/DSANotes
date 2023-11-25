# 1) Recursive
class Solution:
    def reverse(self,head, k):
        # Code here
        curr = head
        prev = None
        count = 0
        while curr and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1
        if next:
            rem_head = self.reverse(curr, k)
            head.next = rem_head        
        return prev

# 2) Iterative
class Solution:
    def reverse(self,head, k):
        # Code here
        curr = head
        prev_first = None
        first_pass = True
        while curr:
            first, prev = curr, None
            count = 0
            while curr and count < k:
                count += 1
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            if first_pass:
                head = prev
                first_pass = not first_pass
            else:
                prev_first.next = prev
            prev_first = first
        return head