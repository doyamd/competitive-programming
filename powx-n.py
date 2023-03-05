class Solution:
    def poww(self,x,n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n%2 ==0:
            return (self.poww(x,n/2)**2)
        else:
            return (self.poww(x,(n+1)/2) * self.poww(x,(n-1)/2))
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -1*n
        return self.poww(x,n)