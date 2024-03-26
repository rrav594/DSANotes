#Function to convert a binary tree to doubly linked list.
class Solution:
    def bToDLL(self,root):
        def dfs(root):
            if not root:
                return None
            if root.left:
                left = dfs(root.left)
                while left.right:
                    left = left.right
                left.right = root
                root.left = left
            if root.right:
                right = dfs(root.right)
                while right.left:
                    right = right.left
                right.left = root
                root.right = right
            return root
        root = dfs(root)
        while root.left:
            root = root.left
        return root


#Function to convert a binary tree to doubly linked list.
class Solution:
    def bToDLL(self,root):
        # do Code here
        self.head = None
        self.prev = None
        
        def dfs(root):
            if not root:
                return 
            
            dfs(root.left)
            if not self.prev:
                self.head = root
                self.prev = root
            else:
                self.prev.right = root
                root.left = self.prev
                self.prev = root
            dfs(root.right)
        dfs(root)
        return self.head
