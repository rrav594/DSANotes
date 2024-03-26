from queue import deque
class Solution:
    def diagonal(self,root):
        #:param root: root of the given tree.
        #return: print out the diagonal traversal,  no need to print new line
        #code here
        ans = []
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            while curr:
                if curr.left:
                    q.append(curr.left)
                ans.append(curr.data)
                curr = curr.right
        return ans
    

class Solution:
    def diagonal(self,root):
        #:param root: root of the given tree.
        #return: print out the diagonal traversal,  no need to print new line
        #code here
        res = []
        if root is None:
            return res
        stack = []
        stack.append(root)
        while stack:
            curr = stack.pop(0)
            while curr:
                res.append(curr.data)
                if curr.left:
                    stack.append(curr.left)
                curr = curr.right        
        return res