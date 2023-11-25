class Solution:
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        mid = sizeOfStack//2
        def delete(s, mid, curr):
            if curr == mid:
                s.pop()
                return
            x = s.pop()
            delete(s, mid, curr+1)
            s.append(x)
            return s
        return delete(s, mid, 0)