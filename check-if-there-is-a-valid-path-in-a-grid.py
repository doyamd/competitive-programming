class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        paths = {
            1: [[0, 1], [0, -1]],
            2: [[1, 0], [-1, 0]],
            3: [[0, -1], [1, 0]],
            4: [[0, 1], [1, 0]],
            5: [[0, -1], [-1, 0]],
            6: [[-1, 0], [0, 1]],
        }
        def inbound(i,j):
            if 0 <= i < m and 0 <= j < n:
                return True
            
        queue = deque([(0,0)])
        visited = {(0, 0)}
        
        while queue:
            x, y = queue.popleft()
            if x == m - 1 and y == n - 1:
                return True
            for dx, dy in paths[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if inbound(nx,ny) and (nx, ny) not in visited:
                    for ndx, ndy in paths[grid[nx][ny]]:
                        if nx + ndx == x and ny + ndy == y:
                            queue.append((nx, ny))
                            visited.add((nx, ny))
                            break
        return False