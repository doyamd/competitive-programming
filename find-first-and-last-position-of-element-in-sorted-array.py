class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or (target < nums[0] or target > nums[-1]):
            return [-1,-1]
        left = bisect.bisect_left(nums,target)
        right = bisect.bisect_right(nums,target)-1
        if nums[left] == target and nums[right] == target:
            return [left,right]
        return [-1,-1]