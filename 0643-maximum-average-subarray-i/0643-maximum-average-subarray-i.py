class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = 0
        sums = 0
        l = k
        avg = -10**4
        while j < len(nums):
            while k > 0:
                sums += nums[j]
                j += 1
                k -= 1
            
            if k == 0:
                avg = max(avg, sums/l)
            sums -= nums[i]
            i += 1
            k += 1
                
        return avg