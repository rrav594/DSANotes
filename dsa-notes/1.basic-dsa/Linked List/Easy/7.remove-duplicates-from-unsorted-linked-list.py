class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        curr = head
        s = set()
        s.add(curr.data)
        while curr.next:
            if curr.next.data in s:
                curr.next = curr.next.next
            else:
                s.add(curr.next.data)
                curr = curr.next
        return head