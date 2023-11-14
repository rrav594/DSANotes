# 1) Using two-stacks
class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        stack1 = [] 
        stack2 = []
        ans = []
        stack1.append(root)
        while stack1 or stack2:
            while stack1:
                curr = stack1.pop()
                ans.append(curr.data)
                if curr.left:
                    stack2.append(curr.left)
                if curr.right:
                    stack2.append(curr.right)
            while stack2:
                curr = stack2.pop()
                ans.append(curr.data)
                if curr.right:
                    stack1.append(curr.right)
                if curr.left:
                    stack1.append(curr.left)
        return ans
    
# 2) Using deque and a flag variable
from queue import deque
class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        if root is None:
            return []
        q = deque()
        q.append(root)
        ans = []
        flag = True
        while q:
            level = []
            for i in range(len(q)):
                curr = q.popleft()
                level.append(curr.data)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if not flag:
                level = level[::-1]
            ans.extend(level)
            flag = not flag
        return ans
