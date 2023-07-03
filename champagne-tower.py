class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0]*x for x in range(1,102)]
        dp[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i+1):
                pour = (dp[i][j] - 1)/2 
                if pour > 0:
                    dp[i+1][j] += pour 
                    dp[i+1][j+1] += pour
        return min(1,dp[query_row][query_glass])