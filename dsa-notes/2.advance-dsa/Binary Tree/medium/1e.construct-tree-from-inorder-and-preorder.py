class Solution:
    def buildtree(self, inorder, preorder, n):
        if n == 0:
            return None
        root = Node(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildtree(inorder[:index], preorder[1:index+1], index)
        root.right = self.buildtree(inorder[index+1:], preorder[index+1:], n-index-1)
        return root
