class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        # Code here
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.mirror(root.left)
        self.mirror(root.right)
        return root