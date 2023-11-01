class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        degree = max(count.values())
        d = {}
        ans ={}
        if degree == 1 or degree == 0:
            return degree
        for i in range(len(nums)):
            if count[nums[i]] == degree:
                if nums[i] not in d:
                    d[nums[i]] = i
                else:
                    ans[nums[i]] = i-d[nums[i]]+1

        return min(ans.values())
        