class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(list)
        for i, j in roads:
            d[i].append(j)
            d[j].append(i)
        maxi = 0
        for i in range(n):
            for j in range(n):
                if i != j :
                    if i in d[j]:
                        maxi = max(maxi, (len(d[i])+len(d[j])-1))
                    else:
                        maxi = max(maxi, (len(d[i])+len(d[j])))

            
        
        
        return maxi