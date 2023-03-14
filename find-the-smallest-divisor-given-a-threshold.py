class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        i = 1
        j = nums[-1]
        ans = j
        while i <= j:
            sums = 0
            mid = (i+j)//2
            for indx in range(len(nums)):
                sums += ceil(nums[indx]/mid)
            if sums <= threshold:
                ans = min(ans,mid)
                j = mid - 1
            elif sums > threshold:
                
                i = mid + 1
            
        return ans