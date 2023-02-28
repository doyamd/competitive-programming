class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        lis = path.split('/')
        #print(lis)
        while i < len(lis):
            if not stack and lis[i] == "" :
                stack.append("/")
                i += 1
            elif stack and stack[-1] != "/" and lis[i] == ""  :
                stack.append("/")
                i += 1
            elif stack and stack[-1] != "/"and lis[i] != "": 
                stack.append("/")
            elif stack and lis[i] == "..":
                if len(stack) > 1:
                    stack.pop()
                    while stack and stack[-1] !="/":
                        stack.pop()
                i += 1
            else:
                if lis[i] != "." and lis[i] != "":
                    stack.append(lis[i])
                i += 1
        if len(stack) > 1  and stack[-1] == "/":
            while stack and stack[-1] =="/" :
                stack.pop()
        return "".join(stack)
                
                
                