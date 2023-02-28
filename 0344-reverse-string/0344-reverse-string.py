class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        def rev(i,j):
            if i >= j: 
                return 
            s[i], s[j] = s[j], s[i]
            
            rev(i+1,j-1)
        rev(i,j)
            
            
            
    
            