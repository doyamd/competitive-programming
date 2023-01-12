#
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #using two pointers
        i=0
        length=len(s)-1
        while i<length:
            s[i],s[length]=s[length],s[i]
            i+=1
            length-=1
