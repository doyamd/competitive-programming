class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5:0, 10:0, 20:0}
        for i in bills:
            if i  == 5:
                d[i] += 1
            elif i < 5:
                return False
            else:
                
                retu = i - 5
                if (d[10] < 1 and retu > 10):
                    if d[5] < 3:
                        return False
                    else:
                        d[5] -= 3
                        d[i] += 1
                        continue
                if d[5] < 1:
                     return False
                
                if retu == 15:
                    d[5] -= 1
                    d[10] -= 1
                if retu == 5:
                    d[5] -= 1
                d[i] += 1
        return True