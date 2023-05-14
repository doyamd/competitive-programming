class Solution:
    def restoreArray(self, graph: List[List[int]]) -> List[int]:
        d = defaultdict(list)
    
        for x,y in graph:
            d[x].append(y)
            d[y].append(x)

        ans = []
        
        for i in d:
            if len(d[i]) == 1:
                ans.append(i)
                break
        
        while d[ans[-1]]:
            node = ans[-1]
            child =d[node][-1]
            d[child].remove(node)
            ans.append(child)

        return ans