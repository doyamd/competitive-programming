class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        conect = defaultdict(list)
        visited = set()
        for x, y in edges:
            conect[x].append(y)
        
        ans = [[] for _ in range(n)]
        res = defaultdict(list)
        
        def dfs(node,x):
            for i in conect[node]:
                if ans[i] and ans[i][-1] == x: continue

                ans[i].append(x)
                dfs(i,x)           
            
       
        for k in range(n):
           dfs(k,k)
            
        return ans