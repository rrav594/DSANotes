class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9)+7
        def pow(x, n):
            if n == 0:
                return 1
            temp = pow(x, n//2)
            if n%2 == 0:
                return (temp*temp)%mod
            else:
                return (x*temp*temp)%mod
        odd = n//2
        even = (n+1)//2
        return (pow(5, even)*pow(4, odd))%mod
        