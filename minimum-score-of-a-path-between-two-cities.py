class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        d = [i for i in range(n+1)]
        
        def find(x):
            if x == d[x]:
                return x
            d[x] = find(d[x])
            return d[x]
        
        
        def union(x, y):
            lx = find(x)
            ly = find(y)
            
            if lx > ly:
                d[ly] = lx
            else:
                d[lx] = ly

        mini = float('inf')
        for x,y,size in roads:
            union(x,y)
        for x,y,size in roads:
            if find(1) == find(x) == find(y):
                mini = min(mini,size)
        return mini