#Function to return a list containing the preorder traversal of the tree.
# 1)Recursive
def preorder(root):
    ans = []
    def dfs(root):
        if root:
            ans.append(root.data)
            dfs(root.left)
            dfs(root.right)
    dfs(root)
    return ans

# 2)Iterative
#Function to return a list containing the preorder traversal of the tree.
def preorder(root):
    if root is None:
        return None
    stack = [root]
    ans = []
    while stack:
        curr = stack.pop()
        ans.append(curr.data)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return ans
# Micro-optimization
def preorder(root):
    stack = [root]
    ans = []
    if root is None:
        return None
    while stack:
        curr = stack.pop()
        while curr:
            ans.append(curr.data)
            if curr.right:
                stack.append(curr.right)
            curr = curr.left
    return ans

# 3)Morris Traversal
def preorder(root):
    if root is None:
        return None
    curr = root
    ans = []
    while curr:
        if curr.left is None:
            ans.append(curr.data)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right
            if prev.right is None:
                prev.right = curr
                ans.append(curr.data)
                curr = curr.left
            else:
                prev.right = None
                curr = curr.right
    return ans
    