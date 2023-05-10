class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        if not pre:
            return True
        d = defaultdict(int)
        graph = defaultdict(list)
        lis = set()
        queue = deque()
        
        for x,y in pre:
            d[x] += 1
        for x, y in pre:
            graph[y].append(x)
            if d[y] == 0 and y not in lis:
                lis.add(y)
                queue.append(y)
            lis.add(y)
            lis.add(x)
            
            
        count = 0
        
        while len(lis) != count and queue:
            
            num = queue.pop()
            count += 1
            for i in graph[num]:
                d[i] -= 1
                if d[i] == 0:
                    queue.append(i)
            print(queue)
        if not queue and len(lis) == count:
            return True