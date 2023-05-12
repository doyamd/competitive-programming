class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = []
        if len(edges) <= 1:
            for i in range(n):
                ans.append(i)
            return ans
        graph = defaultdict(list)
        d = defaultdict(int)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        queue = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                queue.append(i)
        current = n
        while current > 2:
            leng = len(queue)
            current = current - leng
            for l in range(leng):
                node = queue.popleft()
                for i in graph[node]:
                    graph[i].remove(node)
                    if len(graph[i]) == 1:
                        queue.append(i)
        return queue