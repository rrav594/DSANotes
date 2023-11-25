#Function to push an element into stack using two queues.
def push(x):
    # global declaration
    global queue_1
    global queue_2
    queue_2.append(x)
    while queue_1:
        queue_2.append(queue_1.pop(0))
    queue_1, queue_2 = queue_2, queue_1
#Function to pop an element from stack using two queues.     
def pop():
    # global declaration
    global queue_1
    global queue_2
    if not queue_1:
        return -1
    return queue_1.pop(0)