
class Solution:
    def lookandsay(self, n):
        # code here
        def helper(s):
            result = ""
            i = 0
            while i < len(s):
                count = 1
                while i+1 < len(s) and s[i] == s[i+1]:
                    count += 1
                    i += 1
                result += str(count)+s[i]
                i += 1
            return result
        start = "1"
        for i in range(1, n):
            start = helper(start)
        return start
