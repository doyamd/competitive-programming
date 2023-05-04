class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1*stones[i]
        heapify(stones) 
        
        while len(stones) > 1:
            y = ((heappop(stones)) * -1)
            x = ((heappop(stones)) * -1)
            if x != y:
                y = y - x
                heappush(stones,(y*-1))
        if len(stones) == 0:
            return 0
        else:
            return stones[0]*-1