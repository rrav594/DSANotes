def isCircular(head):
    # Code here
    curr = head
    while curr and curr.next != head:
        curr = curr.next
    if curr and curr.next == head:
        return True
    return False


def isCircular(head):
    # Code here
    if head == None:
        return True
    curr = head
    while curr:
        if curr.next == head:
            return True
        curr = curr.next
    return False
    