class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = Counter(s1)
        d2 = {}
        ans = False
        r = 0
        l = 0
        while r < len(s2) and l < len(s2):
            if s2[r] in d1 and d2.get(s2[r],0) < d1.get(s2[r]):
                d2[s2[r]] =d2.get(s2[r],0)+1
                r += 1
            else:
                if s2[l] in d2: 
                    d2[s2[l]] -= 1
                    if d2[s2[l]] == 0:
                        del d2[s2[l]]
                    l += 1   
                else:
                    r += 1 
                    l += 1
            
            if d2== d1:
                ans = True
                break
        return ans
                
                
                
                
        