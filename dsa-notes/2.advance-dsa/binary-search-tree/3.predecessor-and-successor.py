# This function finds predecessor and successor of key in BST.
# It sets pre and suc as predecessor and successor respectively
class Solution:
    def findPreSuc(self, root, pre, suc, key):
        def copy(x, y):
            x.left = y.left
            x.right = y.right
            x.key = y.key
            return x
        curr = root
        while curr:
            if curr.key == key:
                if curr.left:
                    temp = curr.left
                    while temp.right:
                        temp = temp.right
                    copy(pre, temp)
                if curr.right:
                    temp = curr.right
                    while temp.left:
                        temp = temp.left
                    copy(suc, temp)
                return
            elif curr.key < key:
                copy(pre, curr)
                curr = curr.right
            else:
                copy(suc, curr)
                curr = curr.left
    