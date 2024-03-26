  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[-1 for i in range(3)]for i in range(len(points))]
    def helper(day, last):
        if dp[day][last] != -1:
            return dp[day][last]
        if day == 0:
            maxi = float("-inf")
            for i in range(3):
                if i != last:
                    maxi = max(maxi, points[0][i])
            dp[day][last] = maxi
            return dp[day][last]
        maxi = float("-inf")
        for i in range(3):
            if i != last:
                maxi = max(maxi, points[day][i]+helper(day-1, i))
        dp[day][last] = maxi
        return dp[day][last]
    ans = float("-inf")
    for i in range(3):
        ans = max(ans, helper(n-1, i))
    return ans


  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[0 for i in range(3)]for i in range(n)]
    dp[0][0], dp[0][1], dp[0][2] = max(points[0][1], points[0][2]),max(points[0][2], points[0][0]), max(points[0][0], points[0][1])
    for i in range(n):
        for j in range(3):
            for last in range(3):
                if last != j:
                    dp[i][j] = max(dp[i][j], points[i][last]+dp[i-1][last])
    return max(dp[n-1])


  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    prev = [0 for i in range(3)]
    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][2], points[0][0])
    prev[2] = max(points[0][1], points[0][0])
    for i in range(1, n):
        curr = [0 for i in range(3)]
        for j in range(3):
            for last in range(3):
                if j != last:
                    curr[j] = max(curr[j], points[i][last]+prev[last])
        prev = curr
    return max(prev)