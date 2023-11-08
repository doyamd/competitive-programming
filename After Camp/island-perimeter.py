class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        direc = [[1,0],[0,1],[-1,0],[0,-1]]
        def inbound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    break
        ans = 0
        while queue:
            i,j = queue.popleft()
            if (i,j) in visited:
                continue
            visited.add((i,j))
            for x,y in direc:
                if inbound(i+x,j+y) and grid[i+x][j+y] == 1:
                    queue.append((i+x,j+y))
                else:
                    ans += 1
        return ans
                


        