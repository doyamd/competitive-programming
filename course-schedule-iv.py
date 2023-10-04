class Solution:
    def checkIfPrerequisite(self, n: int, pre: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if not pre:
            return [False]*n
        d = defaultdict(set)
        graph = defaultdict(list)
        visited = set()
        for x, y in pre:
            graph[y].append(x)
        ans = []
        for q in queries:
            end,start = q
            heap = [(start)]
            heapq.heapify(heap)
            visited = set()
            found = False
            while heap:
                node = heapq.heappop(heap)
                if node in visited:
                    continue
                visited.add(node)
                for neig in graph[node]:
                    heapq.heappush(heap,(neig))
                if end not in d[start]:
                    d[start].add(node)
                else:
                    found = True
                    break

            if found:
                ans.append(True)
            elif end in d[start]:
                ans.append(True)
            else:
                ans.append(False)
            
            
        return ans