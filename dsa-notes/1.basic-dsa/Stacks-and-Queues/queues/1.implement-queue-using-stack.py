class MyQueue:
    def __init__(self):
        self.arr = []
    #Function to push an element x in a queue.
    def push(self, x):
        self.arr.append(x)
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if len(self.arr):
            return self.arr.pop(0)
        else:
            return -1
         