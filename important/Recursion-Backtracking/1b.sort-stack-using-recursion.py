class Solution:
    def Sorted(self, s):
        def insert(s, item):
            tempStack = []
            while s and item < s[-1]:
                tempStack.append(s.pop())
            s.append(item)
            while tempStack:
                s.append(tempStack.pop())
        if not s:
            return
        top = s.pop()
        self.Sorted(s)
        insert(s, top)
        