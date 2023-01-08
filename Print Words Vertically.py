#https://leetcode.com/problems/print-words-vertically/description/
class Solution:
    def printVertically(self, s: str) -> List[str]:
        words=s.split(' ')
        j=0
        vertical_wrds=[]
        maxi_len=0
        for i  in words:
            maxi_len=max(maxi_len,len(i))
        while j<maxi_len:
            letters=""
            for i in range(len(words)):
                if j+1>len(words[i]):
                    letters+=' '
                else:
                    letters+=words[i][j]

            vertical_wrds.append(letters.rstrip())
            j+=1
        return vertical_wrds
