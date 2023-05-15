class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        if ('0000') in deadends:
            return -1
        queue = deque(['0000'])
        def not_dead(num):
            if num not in deadends:
                return True
        count = -1
        while queue:
            length = len(queue)
            count += 1
            for l in range(length):
                num = queue.popleft()
                if num == target:
                    return count
                if num not in visited:
                    visited.add(num)
                    for i in range(4):
                        add = str((int(num[i]) + 1) % 10)  
                        sub = str((int(num[i]) + 9) % 10)
                        if i == 3:
                            add = num[:i] + add
                            sub = num[:i] + sub
                        elif i == 0:
                            add = add + num[1:] 
                            sub = sub + num[1:]
                        else: 
                            add = num[:i] + add + num[i+1:]
                            sub = num[:i] + sub + num[i+1:]
                        
                        if not_dead(add):
                            queue.append(add)

                        if not_dead(sub):
                            queue.append(sub)
        return -1