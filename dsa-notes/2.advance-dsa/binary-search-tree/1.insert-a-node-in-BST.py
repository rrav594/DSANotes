# 1) Iterative
class Solution:
    #Function to insert a node in a BST. 
    def insert(self,root, Key):
        parent = None
        curr = root
        while curr:
            parent = curr
            if curr.data == Key:
                return root
            elif curr.data < Key:
                curr = curr.right
            else:
                curr = curr.left
        if parent is None:
            return Node(Key)
        elif parent.data < Key:
            parent.right = Node(Key)
        else:
            parent.left = Node(Key)
        return root



# 2) Recursive
class Solution:
    #Function to insert a node in a BST. 
    def insert(self,root, Key):
        # code here
        if root is None:
            return Node(Key)
        elif root.data == Key:
            return root
        elif root.data < Key:
            root.right = self.insert(root.right, Key)
        else:
            root.left = self.insert(root.left, Key)
        
        return root
