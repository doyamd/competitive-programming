class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ans = 0
        pre = [0 for i in range(len(nums)+1)]
        for i in range(len(requests)):
            pre[requests[i][0]] += 1
            pre[requests[i][1]+1] += -1
        pre.pop()
        for i in range(1,len(pre)):
            pre[i] += pre[i-1]
        nums.sort()
        pre = sorted(pre)
        for i in range(len(nums)):
            ans += nums[i] * pre[i]
        return ans%((10**9) +7)


        