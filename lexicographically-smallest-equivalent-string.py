class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        d = defaultdict(str)
        ans = ""
        for i in s1:
            d[i] = i
        for i in s2:
            d[i] = i
        
        for i in range(len(s1)):
            mini = min(d[s1[i]],d[s2[i]])
            reps1 = d[s1[i]]
            reps2 = d[s2[i]]
            for k,v in d.items():
                if v == reps1:
                    d[k] = mini
                if v == reps2:
                    d[k] = mini
      
        for i in baseStr:
            if i not in d:
                ans += i
            else:
                ans += d[i]
        return ans