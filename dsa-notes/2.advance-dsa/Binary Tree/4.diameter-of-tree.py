# 1) Calculationg height in same recurssion
class Solution:
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        # Code here
        diam = [0]
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            diam[0] = max(left + right + 1, diam[0])
            return max(left, right) + 1
        dfs(root)
        return diam[0]
    
    # Same Approach
    class Solution:
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        # Code here
        diam = 0
        def dfs(root):
            nonlocal diam
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            diam = max(left + right + 1, diam)
            return max(left, right) + 1
        dfs(root)
        return diam
    
# 2) Morris Traversal (Solution is incorrect)
class Solution:
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        # Code here
        ans = 0
        curr = root
        while curr:
            if curr.left is None:
                curr = curr.right
            else:
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right
                if pre.right is None:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    leftHeight = 0
                    rightHeight = 0
                    temp = curr.left
                    while temp:
                        leftHeight += 1
                        temp = temp.right
                    temp = curr.right
                    while temp:
                        rightHeight += 1
                        temp = temp.left
                    ans = max(ans, leftHeight+rightHeight+1)
                    curr = curr.right
        return ans