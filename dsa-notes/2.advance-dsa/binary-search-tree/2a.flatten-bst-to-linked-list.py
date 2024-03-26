class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        while root:
            if root.left:
                curr = root.left
                while curr.right:
                    curr = curr.right
                curr.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
        return root