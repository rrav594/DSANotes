from queue import deque
#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    if root is None:
        return []
    q = deque([root])
    ans = []
    while q:
        ans.append(q[0].data)
        for i in range(len(q)):
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return ans