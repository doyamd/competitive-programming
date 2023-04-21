class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(grid)
        col = len(grid[0])
        
        def dfs(i, j):
            if i < 0 or j < 0 or j >= col or i >= row or grid[i][j] != "O" :
                return 
            grid[i][j] = "v"
            direc = [[0,1], [0,-1], [-1, 0], [1, 0]]
            for x,y in direc:
                dfs(i+x,j+y)
       
        for i in range(row):
            dfs(i, 0)
            dfs(i, col-1)
        for j in range(col):
            dfs(0, j)
            dfs(row-1, j)

        for i in range(row):
            for j in range(col):
                if grid[i][j] =="v" :
                    grid[i][j] = "O"
                elif grid[i][j] != "X":
                    grid[i][j] = "X"
        return grid