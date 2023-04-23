class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
       
        factor = set()
        
        def prime(n):
            d = 2
            if n == 1:
                return
            if n == 2:
                factor.add(n)
                return
            while d * d <= n:
                while n % d == 0:
                    factor.add(d)
                    n//=d
                d += 1
            if n > 1:
                factor.add(n)
        for i in nums:
            prime(i)
        return(len(factor))