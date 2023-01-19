class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        target_indx = []
        length = len(nums)
        nums.sort()
        for indx in range(length):
            if target == nums[indx]:
                target_indx.append(indx)
        return target_indx
            