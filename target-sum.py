class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        d = defaultdict(int)

        def path(i,sums):
            # print(d,i, sums)
            if i == n:
                if sums == target:
                    return 1
                else:
                    return 0
            
            if (i,sums) not in d:
               d[(i,sums)] = path(i+1, sums + nums[i]) + path(i+1, sums - nums[i])
                
            return d[(i,sums)]
            
    
        return (path(0,0))