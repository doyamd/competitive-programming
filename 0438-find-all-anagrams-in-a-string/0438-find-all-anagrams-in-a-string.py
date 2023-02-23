class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d1 = Counter(p)
        d2 = {}
        ans = []
        l = len(p)
        i = 0
        j = 0
        while j < len(s):
            d2[s[j]] = d2.get(s[j], 0)+1
            if d1 == d2: 
                ans.append(i)
            if j-i+1 == l:
                d2[s[i]] -= 1
                if d2[s[i]] ==0:
                    d2.pop(s[i])
                    
                i += 1
            j += 1
        return ans
            
                
        