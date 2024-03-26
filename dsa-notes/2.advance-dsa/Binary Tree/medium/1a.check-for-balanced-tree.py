class Solution:
    def isBalanced(self,root):
        def helper(root):
            if root is None:
                return [True, 0]
            left = helper(root.left)
            right = helper(root.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1])<=1
            return [balanced, 1+max(left[1], right[1])]
        return helper(root)[0]
