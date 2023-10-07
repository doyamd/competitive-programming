class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = defaultdict(int)
        visited = set()
        ans = [float('inf')]
        graph = defaultdict(list)
        for f in flights:
            x,y,w = f
            graph[x].append((w,y))
        # print(graph)
        heap = [(0,0,src)]
        while heap:
            # print(heap)
            stops,weight, node = heapq.heappop(heap)
            if (node,stops) in visited:
                continue
            visited.add((node,stops))
            # print(node)
            if node == dst:
                ans.append(weight)
            for w,n in graph[node]:
                new_stop = stops + 1
                if new_stop <= k+1:
                    heappush(heap,(new_stop,weight+w,n))
                    # print(heap)
        # print(ans)
        if min(ans) == float('inf'):
            return(-1)
        return min(ans)