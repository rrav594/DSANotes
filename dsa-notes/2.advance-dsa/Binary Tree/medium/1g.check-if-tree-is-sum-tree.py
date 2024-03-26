class Solution:
    def isSumTree(self,root):
        def total(root):
            if not root:
                return 0
            return root.data+total(root.left)+total(root.right)
        if not root or (not root.left and not root.right):
            return True
        left = total(root.left)
        right = total(root.right)
        return True if (root.data == left+right and self.isSumTree(root.left) and self.isSumTree(root.right)) else False 
        