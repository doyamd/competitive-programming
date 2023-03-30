class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x ^ y
        ans = str(bin(ans)[2:])
        res = ans.count("1")
        return res