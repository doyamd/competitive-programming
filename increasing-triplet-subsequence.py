class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        h1 = float('inf')
        h2 = float('inf')
        for i in nums:
            if i < h1:
                h1 = i
            if i < h2 and i > h1:
                h2 = i
            if i > h2:
                return True

        
        return False