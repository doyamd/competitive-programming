class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ans = True
        opend = ["(","[","{"]
        
        for i in s:
            if i in opend:
                stack.append(i)
            else:
                if stack:
                    poped = stack.pop()
                    if poped == "(" and i != ")" or poped == "[" and i != "]"or poped == "{" and i != "}" :
                        ans = False
                        break
                else:
                    ans = False
        if stack:
            ans = False
        return ans