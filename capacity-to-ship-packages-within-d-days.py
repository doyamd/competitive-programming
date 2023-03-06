class Solution:
    #1 2 3 4 5 6 7 8
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def counting(mid):
            sums = 0
            count = 0
            for j in weights:
                if j > mid:
                   return False
                sums += j
                if sums > mid:
                    count += 1
                    sums = j  
            if sums > 0 :
                count += 1
            return count <= days 
                
        high = sum(weights)
        low = 1
        while low <  high:
            mid = (low+high)//2
            if counting(mid):
                high = mid 
            else :
                low = mid + 1
        return low