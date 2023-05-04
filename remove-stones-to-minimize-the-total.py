class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -1*piles[i]
        heapify(piles)
        for i in range(k):
            num = (heappop(piles)*-1)
            num = ceil(num/2)
            heappush(piles,num*-1)
        sums = 0
        while piles:
            sums += (heappop(piles)*-1)
        return sums