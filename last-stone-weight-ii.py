class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        # print(total)
        half = total//2
        d = {}
        def dfs(i, sums):
            if i == len(stones):
                if sums > half:
                    return 0
                elif sums <= half:
                    return sums
            state = (i, sums)
            if state not in d:  
                if sums > half:
                    d[state] = 0
                elif sums == half:
                    d[state] = sums
                else:
                   d[state] = max(dfs(i+1, sums + stones[i]), dfs(i+1, sums))
            return d[state]
        
        ans = dfs(0,0)
        # print(ans,half)
        return abs((total-ans)-ans)