class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for i in range(len(text2))]for i in range(len(text1))]
        def helper(i, j):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = helper(i-1, j-1)+1
            else:
                dp[i][j] = max(helper(i-1, j), helper(i, j-1))
            return dp[i][j]
        return helper(len(text1)-1, len(text2)-1)
        


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2)+1)]for i in range(len(text1)+1)]
        for i in range(len(text1)+1):
            for j in range(len(text2)+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    continue
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len(text1)][len(text2)]
    


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev = [0 for i in range(len(text2)+1)]
        for i in range(1, len(text1)+1):
            curr = [0 for i in range(len(text2)+1)]
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = 1+prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr
        return prev[-1]