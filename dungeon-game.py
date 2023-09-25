class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        d = {}
        direc = [[1,0],[0,1]]
        

        def inbound(i,j):
            if 0 <= i < len(dungeon) and 0 <= j < len(dungeon[0]):
                return True
        def dp(i,j):
            if i == len(dungeon)-1 and j == len(dungeon[0])-1:
                d[(i,j)] = dungeon[i][j]
                if dungeon[i][j] > 0:
                    d[(i,j)] = 0
                
                return d[(i,j)]
            if (i,j) not in d:
                mini = -(float('inf'))
                for x,y in direc:
                    if inbound(i+x,j+y):
                        mini = max(mini,(dp(i+x,j+y)))
                if mini + dungeon[i][j] > 0:
                    d[(i,j)] = 0
                else:
                    d[(i,j)] = mini + dungeon[i][j]
            return d[(i,j)]
        ans = (dp(0,0))
        if ans >= 0:
            return 1
        # print(d)
        ans = abs(ans) + 1
        return ans