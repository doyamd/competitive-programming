class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        tot = m+n-2
        sub = tot-(n-1)
        su = tot-(m-1)
        return (factorial(tot))//(factorial(sub)*factorial(su))