class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i =1
        j = max(piles)
        mini = j
        
        while i <= j:
            mid = (i+j)//2
            hour = 0
            for k in piles:
                hour += ceil(k/mid)
            if hour <= h:
                j = mid-1
            else:
                i = mid+1
        return j + 1