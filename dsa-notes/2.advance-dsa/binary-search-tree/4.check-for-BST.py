class Solution:
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        def check(root, minn, maxx):
            if not root:
                return True
            if root.data <= minn or root.data >= maxx:
                return False
            return check(root.left, minn, root.data) and check(root.right, root.data, maxx)
        return check(root, -float("inf"), float("inf"))