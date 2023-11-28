class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        def add(stack,s):
            for char in s:
                if char == "#" and stack:
                    _ = stack.pop()
                elif char != "#":
                    stack.append(char)
        add(s1,s)
        add(s2,t)
        print(s1,s2)
        if s1 == s2:
            return True
            