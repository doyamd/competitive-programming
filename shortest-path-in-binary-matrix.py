class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direc = [[1,1],[-1,-1],[-1,1],[1,-1],[1,0],[0,1],[-1,0],[0,-1]]
        path = -1
        if grid[0][0] == 1:
            return -1
        queue = deque()
        queue.append([0,0])
        visited = set()
        visited.add((0,0))
        def inbound(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid) or grid[i][j] == 1:
                return False
            else:
                return True
        count = 0
        while queue:
            length = len(queue)
            count += 1
            for l in range(length):
                r,c = queue.popleft()
                if (r,c) == (len(grid)-1, len(grid)-1):
                    return count
                for x,y in direc:
                    if (r+x,c+y) not in visited and inbound(r+x,c+y):
                        visited.add((r+x,c+y))
                        queue.append([r+x,c+y])
        
        
        return -1