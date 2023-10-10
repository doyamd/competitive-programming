class Solution:
    def strStr(self, hay: str, needle: str) -> int:
        def sub(char,heyy):
            l = ((ord(char)-ord('a')+1)* (27**(len(needle)-1)))
            print(l)
            return heyy - l
        def add(char,heyy):
            heyy = heyy*27
            l = (ord(char)-ord('a')+1)%((10**9)+7)
            return heyy+l
        
        def build(needl):
            nee = 0 
            for char in needl:
                nee = add(char,nee)
            return nee 

        nee = build(needle)
        heyy = build(hay[:len(needle)])
        
        j = 0
        
        for i in range(len(needle),len(hay)):
            if heyy == nee:
                return j
            heyy = sub(hay[j],heyy)
            heyy = add(hay[i],heyy)
            j += 1
        if heyy == nee:
            return j
        return -1