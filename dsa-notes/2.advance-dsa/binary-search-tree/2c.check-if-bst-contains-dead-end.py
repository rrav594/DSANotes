class Solution:
    def isDeadEnd(self, root):
        # Code here
        def helper(root, min, max):
            if not root:
                return False
            if min == max:
                return True
            left = helper(root.left, min, root.data-1)
            right = helper(root.right, root.data+1, max)
            return left or right
        return helper(root, 1, float("inf"))
    


class Solution:
    def isDeadEnd(self, root):
        d = {}
        def storeNode(root):
            if not root:
                return
            d[root.data] = 1
            storeNode(root.left)
            storeNode(root.right)
        def check(root):
            if not root:
                return False
            if not root.left and not root.right:
                pre = root.data-1
                nex = root.data+1
                if pre in d and nex in d:
                    return True
                return False
            return check(root.left) or check(root.right)
        storeNode(root)
        d[0] = 1
        return check(root)