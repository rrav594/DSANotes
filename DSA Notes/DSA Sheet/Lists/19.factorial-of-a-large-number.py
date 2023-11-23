class Solution:
    def factorial(self, N):
        #code here
        ans = [1]
        for x in range(2, N+1):
            carry = 0
            for i in range(len(ans)):
                res = ans[i]*x + carry
                ans[i] = res%10
                carry = res//10
            while carry > 0:
                ans.append(carry%10)
                carry //= 10
        return ans[::-1]
    








class Solution:
    def factorial(self, N):
        #code here
        ans = [1]
        while N > 1:
            carry, size = 0, len(ans) 
            for i in range(size):
                res = ans[i]*N+carry
                ans[i] = res%10
                carry = res//10
            while carry:
                ans.append(carry%10)
                carry = carry//10
            N -= 1
        return ans[::-1]