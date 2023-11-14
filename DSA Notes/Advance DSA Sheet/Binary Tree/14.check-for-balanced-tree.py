#Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalanced(self,root):
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left-right) > 1:
                return float("inf")
            return max(left, right) + 1
        return dfs(root) != float("inf")


#Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalanced(self,root):
        def dfs(root):
            if root is None:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1])<=1
            return [balanced, max(left[1], right[1])+1]
        return dfs(root)[0]