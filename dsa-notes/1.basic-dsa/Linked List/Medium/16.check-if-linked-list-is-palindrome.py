# 1) Using Stack to check - O(n) space 
#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        #code here
        stack = []
        curr = head
        while curr:
            stack.append(curr.data)
            curr = curr.next
        curr = head
        while curr:
            if stack.pop() != curr.data:
                return False
            curr = curr.next
        return True
    
# 2) Constanst space and Efficient Approach
#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        #code here
        def reverse(head):
            curr, prev = head, None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        if head is None:
            return True
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = reverse(slow.next)
        curr = head
        while rev:
            if rev.data != curr.data:
                return False
            rev = rev.next
            curr = curr.next
        return True

