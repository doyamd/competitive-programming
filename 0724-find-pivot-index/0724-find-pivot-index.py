class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        ans = 0
        leftsum = 0
        flag = False
        prefix.append(nums[0])
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1] + nums[i])
        for i in range(len(nums)):
            if leftsum*2 == prefix[len(nums)-1]-nums[i]:
                ans += i
                flag = True
                break
            leftsum += nums[i]
        if not flag:
            ans = -1
        return ans
            
        
        