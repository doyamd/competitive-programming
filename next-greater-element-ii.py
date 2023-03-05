class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1 for i in range(len(nums))]
        for k in range(2):
            for i in range(len(nums)):
                if not stack:
                    stack.append([i,nums[i]])
                if stack and stack[-1][1] < nums[i]:
                    while stack and stack[-1][1] < nums[i]:
                        indx,num = stack.pop()
                        ans[indx] = nums[i]
                    stack.append([i,nums[i]])
                else: 
                    stack.append([i,nums[i]])
        
        return ans