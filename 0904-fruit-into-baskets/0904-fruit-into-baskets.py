class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        i = 0
        j = 0
        ans = 0
        while j < len(fruits):
            d[fruits[j]] = d.get(fruits[j],0)+1
            while len(d) > 2:
                d[fruits[i]] -= 1
                if d[fruits[i]] == 0:
                    del d[fruits[i]]
                i += 1
            ans = max(ans,j-i+1)
            j += 1
        ans = max(ans,j-i)
        return ans
            