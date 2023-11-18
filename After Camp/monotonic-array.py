class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        arr = sorted(nums)
        if arr == nums or arr[::-1] == nums:
            return True
        