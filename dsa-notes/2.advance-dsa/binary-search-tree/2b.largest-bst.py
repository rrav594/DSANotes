class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):
        def helper(root):
            if not root:
                return [float("inf"), float("-inf"), 0]
            if not root.left and not root.right:
                return [root.data, root.data, 1]
            ans = [0, 0, 0]
            left = helper(root.left)
            right = helper(root.right)
            if left[1] < root.data and right[0] > root.data:
                ans[0] = min(root.data, left[0])
                ans[1] = max(root.data, right[1])
                ans[2] = left[2]+right[2]+1
            else:
                ans[0] = float("-inf")
                ans[1] = float("inf")
                ans[2] = max(left[2], right[2])
            return ans
        return helper(root)[2]