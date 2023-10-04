class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        distance = defaultdict(int)
        ans = 0
        for i in range(1,n+1):
            distance[i] = float('inf')
        distance[k] = 0
        heap = [(0,k)]
        heapq.heapify(heap)
        visited = set()
        for node in times:
            graph[node[0]].append((node[1],node[2]))
        while heap:
            dis, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            for neig, w in graph[node]:
                new_dis = dis + w
                if new_dis < distance[neig]:
                    distance[neig] = new_dis
                    heapq.heappush(heap,(new_dis,neig))
        for k, v in distance.items():
            ans = max(ans,v)
        if ans == float('inf'):
            return -1
        return ans