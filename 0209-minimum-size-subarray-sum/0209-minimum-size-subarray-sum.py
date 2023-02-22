class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        sums = nums[0]
        ans = len(nums)
        flag = False
        while j < len(nums):
            if sums < target:
                j += 1
                if j < len(nums):
                    sums += nums[j]
            else:
                while sums >= target:
                    sums -= nums[i]
                    i += 1
                #print(sums)
                ans = min(ans,j-i+2)
                #print(ans)
                flag = True
        
        if not flag:
            ans = 0
        return ans
            
            
            