def frogJump(n: int, heights: List[int]) -> int:
    dp = [-1]*n
    def helper(n):
        if n == 0:
            return 0
        if n == 1:
            return abs(heights[1]-heights[0])
        if dp[n] != -1:
            return dp[n]
        dp[n] = min(abs(heights[n]-heights[n-1])+helper(n-1), abs(heights[n]-heights[n-2])+helper(n-2))
        return dp[n]
    return helper(n-1)


def frogJump(n: int, heights: List[int]) -> int:
    dp = [0]*n
    dp[0] = 0
    dp[1] = abs(heights[1]-heights[0])
    for i in range(2, n):
        jump1 = dp[i-1]+abs(heights[i]-heights[i-1])
        jump2 = dp[i-2]+abs(heights[i]-heights[i-2])
        dp[i] = min(jump1, jump2)
    return dp[n-1]


def frogJump(n: int, heights: List[int]) -> int:
    prev2, prev = 0, abs(heights[1]-heights[0])
    if n == 0:
        return 0
    for i in range(2, n):
        jump1 = abs(heights[i]-heights[i-1])+prev
        jump2 = abs(heights[i]-heights[i-2])+prev2
        curr = min(jump1, jump2)
        prev2 = prev
        prev = curr
    return prev