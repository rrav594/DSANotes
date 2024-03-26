class Solution:
    def toSumTree(self, root) :
        #code here
        if root is None:
            return 0
        old = root.data
        root.data = self.toSumTree(root.left)+self.toSumTree(root.right)
        return old+root.data