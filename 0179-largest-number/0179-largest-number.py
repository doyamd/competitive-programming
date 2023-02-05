class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = ""
        for i in range(len(nums)-1,-1,-1):
            for j in range(i):
                if str(nums[j+1])+str(nums[j]) > str(nums[j])+str(nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        for _ in nums:
            ans += str(_)
        return str(int(ans))