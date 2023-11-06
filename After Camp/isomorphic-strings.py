class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        visited = set()
        taken = set()
        d = {}
        for i, char in enumerate(s):
            if char not in visited:
                if t[i] in taken:
                    return False
                visited.add(char)
                taken.add(t[i])
                d[char] = t[i]
            else:
                if d[char] != t[i]:
                    return False
        return True
