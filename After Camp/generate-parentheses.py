class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(s):
            stack = []
            ans = True
            for i in s:
                if i == '(':
                    stack.append(i)
                else:
                    if stack:
                        poped = stack.pop()
                        if poped == "(" and i != ")" :
                            ans = False
                            break
                    else:
                        ans = False
            if stack:
                ans = False
            return ans
        ans = []
        n *= 2
        def dp(par,count):
            if count == n: 
                if isValid(par):
                    ans.append(par)
                return
            dp(par+'(', count+1)
            dp(par+')',count+1)
            return
        dp('',0)
        return ans


        