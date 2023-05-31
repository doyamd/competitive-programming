class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == n == 1:
            return 1
        d = defaultdict(int)
        direc = [[0,1],[1,0]]
        def inbound(i,j):
            if i >= 0 and j >= 0 and  i < m and j < n:
                return True
            return False
        count = 0
        def path(i,j):
            nonlocal count
            if i == m-1 and j == n-1 :
                count += 1
                return 1
            for x, y in direc:
                if inbound(i+x,j+y):
                    if (i+x,j+y) not in d:
                        d[(i+x,j+y)] += path(i+x,j+y)
                    d[(i,j)] += d[(i+x,j+y)]
            return d[(i,j)]
        path(0,0)
        
        return (d[(1,0)] + d[(0,1)])