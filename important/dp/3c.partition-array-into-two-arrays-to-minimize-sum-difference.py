def minSubsetSumDifference(nums: List[str], n: int) -> int:
    total = sum(nums)
    dp = [[False for i in range(total+1)]for i in range(n)]
    for i in range(n):
        for j in range(total+1):
            if j == 0:
                dp[i][j] = True
                continue
            if i == 0 and nums[i] == j:
                dp[i][j] = True
                continue
            pick = False
            if nums[i] <= j:
                pick = dp[i-1][j-nums[i]]
            notPick = dp[i-1][j]
            dp[i][j] = pick or notPick
    min_ = float("inf")
    for i in range(total+1):
        if dp[n-1][i] == True:
            diff = abs(i-(total-i))
            min_ = min(min_, diff)
    return min_