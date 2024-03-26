def moreSubsequence(n: int, m: int, a: str, b:str) -> str:
    def count(s):
        count = 1
        d = {}
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1
        for i in range(1, len(s)+1):
            dp[i] = dp[i-1]*2
            if s[i-1] in d:
                dp[i] = dp[i]-dp[d[s[i-1]]-1]
            d[s[i-1]] = i
        return dp[len(s)]
    count1 = count(a)
    count2 = count(b)
    if count1 >= count2:
        return a
    return b