class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        time = 0
        visited = set()
        d = defaultdict(list)
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)

        def dfs(node):
            time = 0
            for i in d[node]:
                if i not in visited:
                    visited.add(i)
                    count = dfs(i) 
                    if hasApple[i] or count:
                        time += count + 2
                
                        
            return time
        visited.add(0)
        return dfs(0)