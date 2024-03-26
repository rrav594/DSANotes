class Solution:
    def kthLargest(self,root, K):
        #your code here
        stack = []
        curr = root
        if not curr:
            return
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.right
            curr = stack.pop()
            K -= 1
            if K == 0:
                return curr.data
            curr = curr.left
        return -1


class Solution:
    def kthLargest(self,root, k):
        #your code here
        if not root:
            return
        curr = root
        while curr:
            if not curr.right:
                k -= 1
                if k == 0:
                    return curr.data
                curr = curr.left
            else:
                pre = curr.right
                while pre.left and pre.left != curr:
                    pre = pre.left
                if not pre.left:
                    pre.left = curr
                    curr = curr.right
                else:
                    pre.left = None
                    k -= 1
                    if k == 0:
                        return curr.data
                    curr = curr.left
        return -1
                