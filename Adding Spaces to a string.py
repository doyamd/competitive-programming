#https://leetcode.com/problems/adding-spaces-to-a-string/description/
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=['a']*(len(s)+len(spaces))#assigning randonm string with thr length of s and space
        k=0
        count=0
        while k<len(spaces):
            ans[spaces[k]+count]=" "# giving spaces at the intended indexes
            count+=1
            k+=1
        i=0
        j=0
        while i<len(ans) and j<len(s):# adding s values in the new spaced string
            if ans[i]!=" ":
                ans[i]=s[j]
                j+=1
            i+=1
        spaced_str=''.join(ans)
        return spaced_str
