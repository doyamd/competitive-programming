#https://leetcode.com/problems/largest-perimeter-triangle/
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        i=0
        ans=0
        while i<len(nums)-2:
            if nums[i]+nums[i+1]>nums[i+2] and  nums[i+2]+nums[i]>nums[i+1]  and nums[i+2]+nums[i+1]>nums[i]:
                sumation= nums[i]+nums[i+1]+nums[i+2]
                ans=max(ans,sumation)
            i+=1
        return ans
            
