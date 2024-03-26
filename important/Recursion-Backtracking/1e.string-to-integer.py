class Solution:
    def myAtoi(self, s: str) -> int:
        flag = False
        min_, max_ = -2**31, 2**31-1
        ans = 0
        s = s.strip()
        if len(s) == 0 :
            return 0
        if s[0] == "-":
            flag = True
        i = 1 if (s[0] == "-" or s[0] == "+") else 0
        while i < len(s):
            if not s[i].isdigit():
                break
            ans = 10*ans+int(s[i])
            i += 1
        ans = ans if not flag else -1*ans
        ans = max(ans, min_)
        ans = min(ans, max_)
        return ans
