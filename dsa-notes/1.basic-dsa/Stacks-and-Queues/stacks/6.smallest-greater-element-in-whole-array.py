
def greaterElement (arr, n) : 
    #Complete the function
    d = {}
    l = list(set(arr))
    l.sort()
    for i in range(len(l)):
        d[l[i]] = i
    for i in range(n):
        index = d[arr[i]]
        if index == len(l)-1:
            arr[i] = -10000000
        else:
            arr[i] = l[index+1]
    return arr