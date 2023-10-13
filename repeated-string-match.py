class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = 0
        j = 0
        i = 0
        l = 0
        r = 1
        lps = [0]*len(b)
        while r < len(b):
            if b[r] == b[l]:
                lps[r] += l + 1
                l += 1
                r += 1
            else:
                if l == 0:
                    lps[r] = 0
                    r += 1
                else:
                    l = lps[l-1]
        print(lps)
     
        while i < len(a):
            if  i == 0:
                count += 1
            if a[i] == b[j]:
                i += 1
                i = i%len(a)   
                j += 1
            else:
                
                if not j:
                    i += 1
                elif count > 2:
                    return -1
                else:
                    j = lps[j-1]
                
          
            if j == len(b):
                return count
        print("jj")
        return -1