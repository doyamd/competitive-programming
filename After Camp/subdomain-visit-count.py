class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        ans = []
        for dom in cpdomains:
            num, s = dom.split()
            d[s] += int(num)
            i = 0
            while i < len(s):
                if s[i] == '.':
                    d[s[i+1:]] += int(num)
                i += 1
        for k, v in d.items():
            ans.append(str(v)+ " " + k)
        return ans

       