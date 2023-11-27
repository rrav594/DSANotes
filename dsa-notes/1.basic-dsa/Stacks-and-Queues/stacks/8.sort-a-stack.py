class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        # Code here
        if len(s) == 0:
            return
        x = s.pop()
        self.Sorted(s)
        tempStack = []
        while s and x < s[-1]:
            tempStack.append(s.pop())
        s.append(x)
        while tempStack:
            s.append(tempStack.pop())