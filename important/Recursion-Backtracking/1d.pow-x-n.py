class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        temp = self.myPow(x, n//2)
        if n%2:
            return temp*temp*x
        else:
            return temp*temp