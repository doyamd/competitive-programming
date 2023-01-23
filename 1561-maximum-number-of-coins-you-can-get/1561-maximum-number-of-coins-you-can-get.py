class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i=int (len(piles)/3)
        max_pile=0
        while i < len(piles):
            max_pile += piles[i]
            i+=2
        return max_pile
        