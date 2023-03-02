class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {}
        if len(position) == 1:
            return 1
        
        stack = []
    
        for i in range(len(position)):
            d[position[i]] = speed[i]
        
        di = sorted(d.items(), key=lambda x:x[0], reverse= True )
        print(di)
        for i in range(len(di)):
            if not stack:
                stack.append((target-di[i][0])/di[i][1])
            elif stack and stack[-1] < (target-di[i][0])/di[i][1]:
                stack.append((target-di[i][0])/di[i][1])
        
        return len(stack)