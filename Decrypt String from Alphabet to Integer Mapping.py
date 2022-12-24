#https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/
class Solution:
    def freqAlphabets(self, s: str) -> str:
        letters="0abcdefghijklmnopqrstuvwxyz"
        ans=''
        hold=''
        indx=0
        while indx<len(s):
            if indx+2<len(s) and s[indx+2]=='#':
                hold=hold+s[indx]
                hold=hold+s[indx+1]
                ans=ans+letters[int(hold)]
                hold=''
                indx+=3
                
            else:
                hold+=s[indx]
                ans=ans+letters[int(hold)]
                hold=''
                indx+=1
        return ans
            
