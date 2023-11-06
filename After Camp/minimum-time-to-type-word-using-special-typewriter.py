class Solution:
    def minTimeToType(self, word: str) -> int:
        start = ord('a')
        ans = 0
        for i in word:
            clock = abs(ord(i)-start)
            anti = 26 - abs(ord(i)-start)
            ans += min(clock,anti)+1
            start = ord(i)

        return ans