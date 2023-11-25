def countRev (s):
    # your code here
    res = 0
    temp = 0
    for char in s:
        if char is "{":
            temp += 1
        else:
            if temp == 0:
                res += 1
                temp += 1
            else:
                temp -= 1
    if temp % 2:
        return -1
    return res + temp//2
    


def countRev (s):
    # your code here
    stack = []
    ans = 0
    for i in range(len(s)):
        if s[i] == "{":
            stack.append(s[i])
        else:
            if stack:
                stack.pop()
            else:
                ans += 1
                stack.append("{")
    return -1 if len(stack)%2 else ans+len(stack)//2
    
