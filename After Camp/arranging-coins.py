class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        for i in range(1,n+1):
            n -= i
            count += 1
            # print(n,count)
            if n == 0:
                return count
            elif n < 0:
                return count -1 
            
        return count


        