class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bitt = str(bin(n)[2:])
        for i in range(len(bitt)-1):
            if bitt[i] == bitt[i + 1]:
                return False
        return True