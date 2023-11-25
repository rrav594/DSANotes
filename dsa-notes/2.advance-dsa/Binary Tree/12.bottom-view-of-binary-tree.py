from queue import deque
class Solution:
    def bottomView(self, root):
        # code here
        if root is None:
            return 0
        q = deque()
        q.append([root, 0])
        d = {0:root.data}
        while q:
            curr, line = q.popleft()
            d[line] = curr.data
            if curr.left:
                q.append([curr.left, line-1])
            if curr.right:
                q.append([curr.right, line+1])
        ans = []
        for line in sorted(d.keys()):
            ans.append(d[line])
        return ans
