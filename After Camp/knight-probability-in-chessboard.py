class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        direc = [[2,-1],[2,1],[1,2],[1,-2],[-2,1],[-2,-1],[-1,2],[-1,-2]]
        dp = {}
        def inbound(i,j):
            return 0 <= i < n and  0<= j < n

        def dfs(i,j,k):
            if k<0:
                return 1
            if not inbound(i,j):
                return 0
            if (i,j,k) in dp:
                return dp[(i,j,k)]
            sums = 0
            for x,y in direc:
                sums += dfs(x+i,y+j,k-1)/8
            dp[(i,j,k)] = sums
            return sums

            
        
        return dfs(row,column,k)