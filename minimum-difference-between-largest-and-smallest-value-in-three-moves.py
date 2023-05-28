class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 4:
            return 0
        n = len(nums)-1
        nums.sort()
        
        return (min(nums[n] - nums[3],nums[n-1]-nums[2], nums[n-2] - nums[1], nums[n-3] - nums[0]))