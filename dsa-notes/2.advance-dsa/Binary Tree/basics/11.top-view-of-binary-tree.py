from queue import deque
class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        if root is None:
            return 0
        q = deque()
        q.append([root, 0])
        d = {0:root.data}
        while q:
            curr, line = q.popleft()
            if line not in d:
                d[line] = curr.data
            if curr.left:
                q.append([curr.left, line-1])
            if curr.right:
                q.append([curr.right, line+1])
        ans = []
        for line in sorted(d.keys()):
            ans.append(d[line])
        return ans