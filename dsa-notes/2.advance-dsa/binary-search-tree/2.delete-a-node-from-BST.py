def deleteNode(root, X):
    def minValueNode(root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr
    if root is None:
        return None
    if root.data < X:
        root.right = deleteNode(root.right, X)
    elif root.data > X:
        root.left = deleteNode(root.left, X)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    return root
            