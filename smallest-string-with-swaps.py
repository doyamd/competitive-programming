class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        rep = list(range(len(s)))
        d = defaultdict(list)
        dch = defaultdict(list)
        def find(i):
            if i != rep[i]:
                rep[i] = find(rep[i])
            return rep[i]

        def union(x,y):
            repx = find(x)
            repy = find(y)

            if repx != repy:
                rep[repy] = repx
                
        for x,y in pairs:
            union(x,y)
            
        ans = ["" for _ in range(len(s))]
        
        for i in range(len(rep)):
            anses = find(i)
            d[anses].append(i)
            dch[anses].append(s[i])
        for k,v in d.items():
            index = sorted(d[k])
            charc = sorted(dch[k])
            for i, c in zip(index,charc):
                ans[i] = c
        
        return "".join(ans)