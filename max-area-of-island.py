class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxi = 0
        visited = set()
        def dfs(i, j):
            if i < 0 or j < 0 or j >= len(grid[0]) or i >= len(grid):
                return 
            if grid[i][j] == 0:
                return
            direc = [[0,1], [0,-1], [-1, 0], [1, 0]]
            visited.add((i,j))
            for x, y in direc:
                if (i+x, j+y) not in visited:
                    dfs(i+x, j+y)
        prev = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited:
                    dfs(i,j)
                    maxi = max(maxi, len(visited)-prev)
                    prev = len(visited)

      
        return maxi