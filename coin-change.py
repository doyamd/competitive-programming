class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = {}

        def getcoin(amount, i):
            if amount < 0 or i >= len(coins):
                return float("inf")
            if amount == 0:
                return 0
            curr = (amount, i)
            if curr not in d:
                take = getcoin(amount-coins[i], i)+1
                nottake = getcoin(amount, i+1)
                d[curr] = min(take, nottake)
            return d[curr]
        ans = 0
        ans = getcoin(amount, 0)
        if ans == float("inf"):
            return -1
        return ans