class MyStack:
    # class StackNode:
    # # Constructor to initialize a node
    # def __init__(self, data):
    #     self.data = data
    #     self.next = None
    def __init__(self):
        self.root = None
    def isEmpty(self):
        return True if self.root is None else False
    #Function to push an integer into the stack.
    def push(self, data):
        node = StackNode(data)
        node.next = self.root
        self.root = node
    #Function to remove an item from top of the stack.
    def pop(self):
        if not self.root:
            return -1
        x = self.root
        self.root = x.next
        return x.data