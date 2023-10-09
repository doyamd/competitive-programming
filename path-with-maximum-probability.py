class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        d = defaultdict(int)
        visited = set()
        ans = [0]
        graph = defaultdict(list)
        for f in range(len(edges)):
            x,y = edges[f]
            w = succProb[f]
            graph[x].append((w,y))
            graph[y].append((w,x))
        # print(graph)
        heap = [(-1,start_node)]
        while heap:
            # print(heap)
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if node == end_node:
                return(-(weight))
            # print(node)
            for w,n in graph[node]:
                new_w = weight*w
                heappush(heap,(new_w,n))
                    # print(heap)
        # print(ans)
        return 0