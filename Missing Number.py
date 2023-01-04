#https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d={}
        ans=0
        for i in nums:
            d[i]=1
        for j in range(len(nums)+1):
             if j not in d.keys():
                ans=j
                break
        return ans
