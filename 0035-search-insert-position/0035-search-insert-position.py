class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        ans = -1
        while i< len(nums): 
            if target == nums[i]:
                ans = i
                break
            elif target < nums[i]:
                ans = i
                break
            i += 1
        if ans == -1:
            ans = i
        return ans