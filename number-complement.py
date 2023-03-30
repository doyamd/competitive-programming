class Solution:
    def findComplement(self, num: int) -> int:
        bitt = str(bin(num))
        ans = ""

        for i in bitt[2:]:
            if i == "0":
                ans += "1"
            else :
                ans += "0"
          
        return int(ans,2)