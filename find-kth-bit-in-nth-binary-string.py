class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def newstring(num,strg):
            if num == 0:
                return strg[k-1]
            new = ''   
            for i in strg:
                if i == '0':
                    new += '1'
                else:
                    new += '0'
            num -= 1
            new = new[::-1]
            ans = strg + '1' + new
            return(newstring(num,ans))
        return (newstring(n-1,'0'))