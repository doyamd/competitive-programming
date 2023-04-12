class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        d = defaultdict(list)
        visited = set()
        count = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if i != j and isConnected[i][j] == 1:
                    d[i+1].append(j+1)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i in d[node]:
                dfs(i)
        for i in range(len(isConnected[0])):
            if i+1 not in visited:
                count += 1
                dfs(i+1)
        return count