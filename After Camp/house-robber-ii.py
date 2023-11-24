class Solution:
    def rob(self, nums: List[int]) -> int:
        d = {}
        if len(nums) == 1:
            return nums[0]
        def dp(i,valid):
            if i == len(nums)-1:
                if valid:
                    return nums[i]
                if nums[i] > nums[0]:
                    return nums[i] - nums[0]
                return 0
            

            if i >= len(nums):
                return 0

            state = (i, valid)
            if (i, valid) not in d:
                d[(i, valid)] = max(dp(i+2,valid),dp(i+3,valid)) + nums[i]
            return d[(i, valid)] 

    

        return max(dp(0,False),dp(1,True))