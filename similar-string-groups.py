class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        rep = {}
        for s in strs:
            rep[s] = s
        ans = set()
        def comp(main, word):
            i = 0
            count = 0
            while i < len(main):
                if main[i] != word[i]:
                    count += 1
                i += 1
            return count <= 2
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

        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                if comp(strs[i],strs[j]):
                    union(strs[i],strs[j])
        for s in strs:
            ans.add(representative(s))
        return len(ans)