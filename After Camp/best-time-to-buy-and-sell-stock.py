class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        i = 0
        j = 1
        while j < len(prices):
            if prices[i] < prices[j]:
                ans = max(ans, prices[j] - prices[i])
                j += 1
            else:
                i = j 
                j += 1

        return ans