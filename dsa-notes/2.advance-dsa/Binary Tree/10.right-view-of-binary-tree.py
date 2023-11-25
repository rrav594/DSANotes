from queue import deque
class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        if root is None:
            return []
        q = deque([root])
        ans = []
        while q:
            ans.append(q[-1].data)
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return ans

