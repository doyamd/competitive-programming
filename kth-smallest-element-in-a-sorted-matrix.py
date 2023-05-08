class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        queue = deque([(0,0)])
        visited = set()
        direc = [[0,1]]
        def inbound(i,j):
            if i < 0 or j >= len(matrix) or j < 0 or i >= len(matrix):
                return False
            else:
                return True
        count = 0
        while queue:
            i,j = queue.popleft()
            count += 1
            if count == k:
                return matrix[i][j]
            if (i,j) not in visited:
                visited.add((i,j))
                for x,y in direc:
                    if inbound(i+x,j+y):
                        queue.append((i+x,j+y))
                    elif inbound(i+1,0):
                        queue.append((i+1,0))