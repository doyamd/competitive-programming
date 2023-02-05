class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        ans = []
        for i in range(len(s)):
            d[s[i]] = i
        
        j = 0
        while j < len(s):
            maxi = d[s[j]]
            i = j
            while i < maxi:
                if maxi < d[s[i]]:
                    maxi = d[s[i]]
                i += 1
            ans.append(maxi - j + 1)
            j = maxi + 1
          
            
        return ans