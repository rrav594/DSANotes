def isSubset( a1, a2, n, m):
    d = {}
    if m > n:
        return "No"
    for i in range(n):
        d[a1[i]] = d.get(a1[i], 0)+1
    for i in range(m):
        if a2[i] in d and d[a2[i]] > 0:
            d[a2[i]] -= 1
        else:
            return "No"
    return "Yes"