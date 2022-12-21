#https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num= str(x)
        i=0
        j=len(num)-1
        ans=True
        while i<=j:
            if(num[i]!=num[j]):
                ans=False
            i+=1
            j-=1
        return ans 
