def minimizeCost(n : int, k : int, heights : List[int]) -> int:
    dp = [-1]*n
    def helper(n):
        if n == 0:
            return 0
        if n == 1:
            return abs(heights[1]-heights[0])
        if dp[n] != -1:
            return dp[n]
        min_ = float("inf")
        for i in range(1, k+1):
            if n-i >= 0:
                jump = abs(heights[n]-heights[n-i])+helper(n-i)
                min_ = min(jump, min_)
        dp[n] = min_
        return dp[n]
    return helper(n-1)


def minimizeCost(n : int, k : int, heights : List[int]) -> int:
    dp = [0]*n
    dp[0] = 0
    if n == 1:
        return 0
    dp[1] = abs(heights[1]-heights[0])
    for i in range(2, n):
        min_ = float("inf")
        for j in range(1, k+1):
            if i-j >= 0:
                jump = abs(heights[i]-heights[i-j])+dp[i-j]
                min_ = min(min_, jump)
        dp[i] = min_
    return dp[n-1] 