# Node Class:
# class Node:
#     def _init_(self,val):
#         self.data = val
#         self.left = None
#         self.right = None
#         '''

# 1) Using level order traversal
from queue import deque
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        h = 0
        q = deque()
        q.append(root)
        while q:
            h += 1
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return h

# 2) Depth First Search
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        def dfs(root):
            if not root:
                return 0
            return max(dfs(root.left), dfs(root.right)) + 1
        return dfs(root)