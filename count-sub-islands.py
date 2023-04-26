class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        maxi = 0
        visited = set()
        self.flag = True
        def dfs(i, j):
            if i < 0 or j < 0 or j >= len(grid2[0]) or i >= len(grid2):
                return 
            if grid2[i][j] == 0:
                return
            direc = [[0,1], [0,-1], [-1, 0], [1, 0]]
            visited.add((i,j))
            if grid1[i][j] == 0:
                self.flag = False
           
            for x, y in direc:
                if (i+x, j+y) not in visited:
                    dfs(i+x, j+y)
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if (i,j) not in visited and grid2[i][j] == 1:
                    dfs(i,j)
                    if self.flag:   
                        count += 1
                self.flag = True
           
        return count