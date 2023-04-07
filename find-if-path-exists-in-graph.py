class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d= defaultdict(list)
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)
        visited = set()
        visited.add(source)
        def dfs(node):
            if node == destination:
                return True
            lis = d[node]
            visited.add(node)
            for i in lis:
                if i not in visited and dfs(i):
                   return True
                
        return dfs(source)