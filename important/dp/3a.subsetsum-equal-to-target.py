def subsetSumToK(n, k, arr):
    dp = [[-1 for i in range(k+1)]for i in range(n)]
    def helper(n, k):
        if dp[n][k] != -1:
            return dp[n][k]
        if k == 0:
            return True
        if n == 0:
            return arr[0]==k
        notPick = helper(n-1, k)
        pick = False
        if arr[n] <= k:
            pick = helper(n-1, k-arr[n])
        dp[n][k] = pick or notPick
        return dp[n][k]
    return helper(n-1, k)
    
    
def subsetSumToK(n, k, arr):
    dp = [[False for i in range(k+1)]for i in range(n)]
    for i in range(n):
        for j in range(k+1):
            if j == 0:
                dp[i][j] = True
                continue
            if i == 0:
                if arr[i] == j:
                    dp[i][j] = True
                    continue
            notPick = dp[i-1][j]
            pick = False
            if arr[i] <= j:
                pick = dp[i-1][j-arr[i]]
            dp[i][j] = pick or notPick
    return dp[n-1][k]



def subsetSumToK(n, k, arr):
    prev = [False for i in range(k+1)]
    for i in range(k+1):
        if i == 0:
            prev[i] = True
        else:
            if arr[0] == i:
                prev[i] = True
    for i in range(1, n):
        curr = [False for i in range(k+1)]
        for j in range(k+1):
            if j == 0:
                curr[j] = True
                continue
            notPick = prev[j]
            pick = False
            if arr[i] <= j:
                pick = prev[j-arr[i]]
            curr[j] = pick or notPick
        prev = curr
    return prev[-1]
            