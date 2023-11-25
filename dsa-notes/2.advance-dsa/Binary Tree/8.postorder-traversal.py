# 1)Recursive
#Function to return a list containing the postorder traversal of the tree.
def postOrder(root):
    # code here
    ans = []
    def dfs(root):
        if root:
            dfs(root.left)
            dfs(root.right)
            ans.append(root.data)
    dfs(root)
    return ans

# 2)Iterative
def postOrder(root):
    # code here
    stack1 = [root]
    stack2 = []
    while stack1:
        curr = stack1.pop()
        stack2.append(curr)
        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)
    while stack2:
        stack1.append(stack2.pop().data)
        # curr = stack2.pop()
        # stack1.append(curr.data)
    return stack1

# 3)Morris Traversal
def postOrder(root):
    # code here
    curr = root
    if curr is None:
        return None
    ans = []
    while curr:
        if curr.right is None:
            ans.append(curr.data)
            curr = curr.left
        else:
            prev = curr.right
            while prev.left and prev.left != curr:
                prev = prev.left
            if prev.left is None:
                prev.left = curr
                ans.append(curr.data)
                curr = curr.right
            else:
                prev.left = None
                curr = curr.left
    return ans[::-1]