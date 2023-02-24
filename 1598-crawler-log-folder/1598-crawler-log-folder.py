class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        i = 0
        ans = 0
        for i in logs:
            if stack and i == "../":
                stack.pop()
            elif (i == "./") or (not stack and i == "../"):
                continue
            else:
                stack.append(i)
            
    
        while stack:
            ans += 1
            stack.pop()
        return ans
                
            
            