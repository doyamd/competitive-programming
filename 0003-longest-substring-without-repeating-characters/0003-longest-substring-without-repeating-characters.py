class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = 0
        d = {}
        
        i = 0 
        j = 0
        while j < len(s):
            d[s[j]] = d.get(s[j],0)+1
            #print(d)
            while d.get(s[j]) > 1:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    d.pop(s[i])
                i += 1
            ans = max(ans,len(d))
            j += 1
        return ans