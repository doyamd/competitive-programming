class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int: 
        d= {}
        def dp(i,j):
            if i == len(triangle)-1 and j < i+1:
                return triangle[i][j]
            
            if i >= len(triangle) or j > i+1:
                return 0

            state = (i, j)
            if state not in d:
                d[state] = min(dp(i+1,j),dp(i+1,j+1)) + triangle[i][j]
            return d[state] 

        return dp(0,0)