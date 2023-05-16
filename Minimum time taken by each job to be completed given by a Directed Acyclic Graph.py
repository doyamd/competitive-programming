from typing import List
from collections import defaultdict, deque

from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        ans = [0 for _ in range(n)]
        d = defaultdict(list)
        length = defaultdict(int) 
        for x,y in edges:
            d[x].append(y)
            length[y] += 1
        queue = deque()
        for i in range(1,n+1):
            if length[i] == 0:
                queue.append(i)
        # print(queue)
        while queue:
            num = queue.popleft()
            ans[num-1] += 1
            for i in d[num]:
                ans[i-1] = max(ans[i-1],ans[num-1])
                length[i] -= 1
                if length[i] == 0:
                    queue.append(i)
                
        return ' '.join([str(v) for v in ans])
