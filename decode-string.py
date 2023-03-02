class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            letter = ""
            num = ""
            temp = ""
            if s[i] >= "a" and  s[i] <= "z" :
                while i < len(s) and s[i] >= "a" and  s[i] <= "z" and s[i] !="]":
                    temp += s[i]
                    i += 1
                stack.append(temp)
                i -= 1
            elif s[i] >= '0' and s[i] <= '9' :
                while i < len(s) and s[i] >= '0' and s[i] <= '9' and s[i] !="[":
                    temp += s[i]
                    i += 1
                stack.append(temp)
                i -= 1
                
            elif s[i] == "]":
                while stack and not stack[-1].isdigit():
                    
                    letter = stack.pop() + letter
                if stack:
                    num += stack.pop()
                
                    word = letter * int(num)
                    stack.append(word)

            i += 1
        if stack and stack[-1].isdigit():
            stack.pop()
        return "".join(stack)