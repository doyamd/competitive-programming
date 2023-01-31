class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        ans = []
        while i*i <= c:
            ans.append(i*i)
            i += 1
        for num in ans:
            if sqrt(c - num) == int(sqrt(c - num)):
                return True
                break
        return False