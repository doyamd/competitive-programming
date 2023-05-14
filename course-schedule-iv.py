class Solution:
    def checkIfPrerequisite(self, n: int, pre: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if not pre:
            return [False]*n
        conect = defaultdict(list)
        visited = set()
        for x, y in pre:
            conect[x].append(y)
        
        ans = [[] for _ in range(n)]
        answer = [False for _ in range(len(queries))]
        res = defaultdict(list)
        
        def dfs(node,x):
            for i in conect[node]:
                if ans[i] and ans[i][-1] == x: continue

                ans[i].append(x)
                dfs(i,x)           
            
        for k in range(n):
           dfs(k,k)
        
        for i in range(len(queries)):
            if queries[i][0] in ans[queries[i][1]]:
                answer[i] = True

        return answer