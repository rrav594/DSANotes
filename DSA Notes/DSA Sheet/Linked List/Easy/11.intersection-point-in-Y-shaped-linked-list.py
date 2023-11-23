#Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1,head2):
    #code here
    s = set()
    while head1:
        s.add(head1)
        head1 = head1.next
    while head2:
        if head2 in s:
            return head2.data
        head2 = head2.next
    return -1