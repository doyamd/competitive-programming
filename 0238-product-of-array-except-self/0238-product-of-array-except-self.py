class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [nums[0]]
        ans = [0 for i in range(len(nums))]
        back = [0 for i in range(len(nums))]
        back[-1] = nums[-1]
        for i in range(1,len(nums)):
            forward.append(forward[i-1]*nums[i])
        for i in range(len(nums)-2,-1,-1):
            back[i] = nums[i] *back[i+1]
            
        for i in range(len(nums)):
            if i == 0:
                left = 1
                right = back[i+1]
            elif i == len(nums) - 1:
                right = 1
                left = forward[i-1] 
            else:
                left = forward[i-1] 
                right = back[i+1]
            ans[i] = left*right
        return ans
            
                
                 
        