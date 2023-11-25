from queue import deque
class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root ):
        # Code here
        q = deque()
        q.append(root)
        res = []
        while q:
            curr = q.popleft()
            res.append(curr.data)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return res
        