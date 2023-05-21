class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = defaultdict(int)
        
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] not in d:
                    d[accounts[i][j]] = i
                if d[accounts[i][j]] != i:
                    temp = d[accounts[i][j]]
                    for k,v in d.items():
                        if v == temp:
                            d[k] = i
        
        ans = defaultdict(list)
        for k,v in d.items():
            ans[v].append(k)
        
        res = [[] for _ in range(len(ans))]
        i = 0
        for k,v in ans.items():
            res[i].append(accounts[k][0])
            v = sorted(v)
            res[i].extend(v)
            i += 1
        
        return res