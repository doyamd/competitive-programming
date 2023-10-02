class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            if len(stack) >= k-1:
                temp = stack[len(stack)-k+1:]
                arr = [s[i]]*(k-1)
                if temp == arr: 
                    for x in range(k-1):
                        _= stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return ''.join(stack)