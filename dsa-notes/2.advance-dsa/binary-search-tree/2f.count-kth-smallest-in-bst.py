class Solution:
    # Return the Kth smallest element in the given BST 
    def KthSmallestElement(self, root, K): 
        #code here.
        if not root:
            return
        curr = root
        while curr:
            if not curr.left:
                K -= 1
                if K == 0:
                    return curr.data
                curr = curr.right
            else:
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right
                if not pre.right:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    K -= 1
                    if K == 0:
                        return curr.data
                    curr = curr.right
        return -1
    

class Solution:
    # Return the Kth smallest element in the given BST 
    def KthSmallestElement(self, root, K): 
        #code here.
        stack = []
        curr = root
        if not curr:
            return
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            K -= 1
            if K == 0:
                return curr.data
            curr = curr.right
        return -1