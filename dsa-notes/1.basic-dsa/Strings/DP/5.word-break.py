# 1) Recursive
def wordBreak(line, dictionary):
    # Complete this function
    size = len(line)
    if size == 0:
        return True
    for i in range(1, size+1):
        if line[:i] in dictionary and wordBreak(line[i:size], dictionary):
            return True
    return False


# 2) Dp
def wordBreak(s, dictionary):
    # Complete this function
    dp = [False for i in range(len(s) + 1)]
    # dp[0] is true because an empty string can always be segmented.
    dp[0] = True
    for i in range(len(s) + 1):
        for j in range(i):
            if dp[j] and s[j: i] in dictionary:
                dp[i] = True
                break
    return dp[len(s)]
