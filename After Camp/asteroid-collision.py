class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for i in range(1,len(asteroids)):
            ass = asteroids[i]
            flag = True
            while stack and flag and ((stack[-1] >= 0 and ass < 0)):
                num = stack.pop()
                if abs(num) > abs(ass):
                    ass = num
                elif abs(num) == abs(ass):
                    flag = False
            if flag:
                stack.append(ass)
        return stack
            



        