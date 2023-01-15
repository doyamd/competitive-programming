class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        n=len(grid)
        res=[[0 for i in range(n-2)] for j in range(n-2)]
        for r in range(n-2):
            for c in range(n-2):
                maxi=grid[r][c]
                for row in range(r, r+3):
                    for col in range(c, c+3):
                           maxi=max(maxi,grid[row][col])
                res[r][c]=maxi
        return res
                           