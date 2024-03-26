def findWays(arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [[-1 for i in range(k+1)]for i in range(n)]
    def helper(n, k):
        if k == 0:
            return 1
        if n == 0:
            return 1 if arr[0] == k else 0
        if dp[n][k] != -1:
            return dp[n][k]
        notPick = helper(n-1, k)
        pick = 0
        if arr[n] <= k:
            pick = helper(n-1, k-arr[n])
        dp[n][k] = pick+notPick
        return dp[n][k]
    return helper(n-1, k)



def findWays(arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [[0 for i in range(k+1)]for i in range(n)]
    for i in range(n):
        for j in range(k+1):
            if j == 0:
                dp[i][j] = 1
                continue
            if i == 0 and arr[0] == j:
                dp[i][j] = 1
                continue
            dp[i][j] = dp[i-1][j]
            if arr[i] <= j:
                dp[i][j] += dp[i-1][j-arr[i]]
    return dp[n-1][k]



def findWays(arr: List[int], k: int) -> int:
    prev = [0 for i in range(k+1)]
    prev[0] = 1
    n = len(arr)
    for i in range(k+1):
        if arr[0] == i:
            prev[i] = 1
    for i in range(1, n):
        curr = [0 for i in range(k+1)]
        for j in range(k+1):
            if j == 0:
                curr[j] = 1
                continue
            curr[j] = prev[j]
            if arr[i] <= j:
                curr[j] += prev[j-arr[i]]
        prev = curr
    return prev[-1]