class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        conect = defaultdict(list)
        d = defaultdict(int)
        for i in range(len(graph)):
            for j in graph[i]:
                conect[j].append(i)
        for i in range(len(graph)):
            d[i] += len(graph[i])
        ans = []
        queue = deque()
        
        for i in range(len(graph)):
            if d[i] == 0:
                queue.append(i)
        
        while queue:
            num = queue.pop()
            ans.append(num)
            for i in conect[num]:
                d[i] -= 1
                if d[i] == 0:
                    queue.append(i)
        ans.sort()
        return ans