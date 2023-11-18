class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        n=len(strs)
        longest =strs[0]
        for j in range(len(longest)):
           if j>len(strs[n-1]):
               longest =longest[:j]
           if longest[j]!=strs[n-1][j]:
               longest=longest[:j]
               break 
            

       
        return longest

             