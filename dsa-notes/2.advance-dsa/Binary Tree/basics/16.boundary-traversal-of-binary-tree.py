class Solution:
    def printBoundaryView(self, root):
        # Code here
        res = []
        def isLeaf(root):
            if not root.left and not root.right:
                return True
            return False
        def left(root):
            if not root:
                return 
            curr = root
            while curr:
                if curr.left or curr.right:
                    res.append(curr.data)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right
        def right(root):
            stack = []
            if not root:
                return
            curr = root.right
            while curr:
                if curr.left or curr.right:
                    stack.append(curr.data)
                if curr.right:
                    curr = curr.right
                else:
                    curr = curr.left
            while stack:
                res.append(stack.pop())
        def leaf(root):
            if not root:
                return
            leaf(root.left)
            if not root.left and not root.right:
                res.append(root.data)
            leaf(root.right)
        if not root:
            return
        res.append(root.data)
        left(root.left)
        leaf(root.left)
        leaf(root.right)
        right(root)
        return res