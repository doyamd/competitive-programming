class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = 0
        ans = sums = sum(nums[:k])
        
        for j in range(k,len(nums)):
            sums = sums + nums[j] - nums[i]
            i += 1
            
            if sums > ans:
                ans = sums
                
        return ans/k