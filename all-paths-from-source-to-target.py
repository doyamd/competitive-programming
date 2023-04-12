class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for i in range(len(graph)):
            d[i].extend(graph[i])
        des = len(graph)-1
        ans = []
        
        def dfs(num, arr):
            nonlocal ans
            if num == des:
                ans.append(arr + [num])
                return
            if not d[num]:
                return
            
            for i in d[num]:
                dfs(i,arr + [num])
        dfs(0,[])
        return ans