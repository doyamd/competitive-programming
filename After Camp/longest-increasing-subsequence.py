class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            maxi = 1
            for j in range(i-1,-1,-1):
                if nums[i] > nums[j]:
                    maxi = max(maxi,dp[i]+dp[j])
            dp[i] = maxi
        return max(dp)
                    


        