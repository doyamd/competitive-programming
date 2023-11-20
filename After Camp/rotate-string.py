class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        first = goal[0]
        for i in range(len(s)):
            if s[i] == first and s[i:] + s[:i] == goal:
                return True

