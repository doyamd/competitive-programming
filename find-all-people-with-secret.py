class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        d = defaultdict(list)
        rep = {}
        ans = []
        for i in range(n):
            rep[i] = i
        for meet in meetings:
            d[meet[2]].append(meet[:2])
        def representative(x):
            if x not in rep:
                return x
            if x == rep[x]:
                return x
            rep[x] = representative(rep[x])
            return rep[x]
            
        def union(x, y):
            xrep = representative(x)
            yrep = representative(y)
            
            if xrep == yrep:
                return
            if xrep < yrep:
                rep[yrep] = xrep
            elif xrep > yrep:
                rep[xrep] = yrep
        union(0,firstPerson)
        d = OrderedDict(sorted(d.items()))
        for key, val in d.items():
            for v in val:
                print(v )
                union(v[0],v[1])
            for v in val:
                if representative(v[0]) != 0:
                    rep[v[0]] = v[0]
                if representative(v[1]) != 0:
                    rep[v[1]] = v[1]
        
        for k, v in rep.items():
            if v == 0:
                ans.append(k)
        
        return ans