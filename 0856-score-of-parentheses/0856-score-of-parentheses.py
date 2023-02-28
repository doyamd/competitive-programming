class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        opend = 0
        i = 0
        while i < len(s):
            if  s[i] == "(":
                opend += 1
                i += 1
            else:
                opend -= 1
                ans += 2**opend
                i += 1
                while i < len(s) and s[i] == ")":
                    opend -= 1
                    i += 1
            
        return ans