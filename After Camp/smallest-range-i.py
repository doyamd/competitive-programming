class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        mini = nums[0]
        maxi = nums[-1]
        if mini == maxi:
            return 0
        mini = mini + k
        if abs(maxi-mini) <= k:
            return 0
        else:
            return (abs(mini-(maxi-k)))
        