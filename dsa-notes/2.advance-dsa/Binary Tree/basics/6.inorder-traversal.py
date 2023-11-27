# 1) Recursive
#Function to return a list containing the inorder traversal of the tree. 
class Solution:
    def InOrder(self,root):
        # code here
        res = []
        def dfs(root):
            if root is None:
                return 
            dfs(root.left)
            res.append(root.data)
            dfs(root.right)
        dfs(root)
        return res
    
# 2)Iterative
class Solution:
    def InOrder(self,root):
        # code here
        stack = []
        if not root:
            return
        ans = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                ans.append(curr.data)
                curr = curr.right
        return ans
    
# 3)Morris Traversal
class Solution:
    def InOrder(self,root):
        # code here
        curr = root
        if curr is None:
            return None
        ans = []
        while curr:
            if curr.left is None:
                ans.append(curr.data)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    ans.append(curr.data)
                    curr = curr.right
        return ans