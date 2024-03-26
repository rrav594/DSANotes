class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []
        def generate(open, close):
            if open == close == n:
                ans.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                generate(open+1, close)
                stack.pop()
            if close < open:
                stack.append(")")
                generate(open, close+1)
                stack.pop()
        generate(0, 0)
        return ans