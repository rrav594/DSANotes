def reverseStack(stack: List[int]) -> None:
    def insert(stack, item):
        if not stack:
            stack.append(item)
            return
        top = stack.pop()
        insert(stack, item)
        stack.append(top)
    if not stack:
        return
    top = stack.pop()
    reverseStack(stack)
    insert(stack, top)