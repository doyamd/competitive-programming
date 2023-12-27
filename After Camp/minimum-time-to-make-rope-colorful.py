class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        i = 0
        j = 0

        while i < len(neededTime) and j < len(neededTime):
            tot = 0
            maxi = 0

            while j < len(neededTime) and colors[i] == colors[j]:
                tot += neededTime[j]
                maxi = max(maxi, neededTime[j])
                j += 1

            ans += tot - maxi
            i = j

        return ans
