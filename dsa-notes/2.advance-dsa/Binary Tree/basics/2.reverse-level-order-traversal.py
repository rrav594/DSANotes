'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
from queue import deque
def reverseLevelOrder(root):
    # code here
    q = deque()
    q.append(root)
    res = deque()
    while q:
        curr = q.popleft()
        res.appendleft(curr.data)
        if curr.right:
            q.append(curr.right)
        if curr.left:
            q.append(curr.left)
    return res
