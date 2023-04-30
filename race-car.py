class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0,1,0)])
        visited = set()
        
        while queue:
            pos, speed, instr = queue.popleft()

            if pos == target:
                return instr
            if (pos,speed) not in visited:
                visited.add((pos,speed))
                queue.append((pos + speed,speed * 2,instr + 1))
                if(pos+speed > target and speed > 0) or( pos+speed<target and speed < 0):
                    if speed > 0:
                        speed = -1
                    else:
                        speed = 1
                    queue.append((pos,speed ,instr + 1))